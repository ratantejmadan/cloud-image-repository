from flask import Flask
from flask import render_template, redirect, url_for, flash
from flask import request
import boto3
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, LoginManager, login_user, login_required, \
    current_user, logout_user

access_key = "AWS ACCESS KEY GOES HERE"
secret = "AWS SECRET GOES HERE"
aws_bucket = "AWS BUCKET NAME GOES HERE"

app = Flask(__name__)

app.config['SECRET_KEY'] = "darthvador"
app.config[
    'SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:Kelvin49" \
                                 "@imagerepository.cj6nhppejj5w.us-east-1.rds" \
                                 ".amazonaws.com:5432/myimages"

db = SQLAlchemy(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    images = db.Column(db.ARRAY(db.String(1000)))


class PublicImages(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String(1000))


@app.route('/')
def main():
    return render_template("home.html")


@app.route('/home')
def home():
    return render_template("home.html")


@app.route('/signup')
def signup():
    return render_template("signup.html")


@app.route('/signup', methods=['POST'])
def user_signup():
    email = request.form.get('email')
    username = request.form.get('username')
    password = request.form.get('password')

    email_check = User.query.filter_by(email=email).first()
    username_check = User.query.filter_by(username=username).first()
    if email_check or username_check:
        flash('Email Address or Username already exists. ')
        return redirect(url_for("signup"))

    # new user
    new_user = User(email=email, username=username,
                    password=generate_password_hash(password, method='sha256'),
                    images=[])
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for("login"))


@app.route('/login')
def login():
    return render_template("login.html")


@app.route('/login', methods=['POST'])
def user_login():
    username = request.form.get('username')
    password = request.form.get('password')
    remember = False

    if request.form.get('remember'):
        remember = True

    user = User.query.filter_by(username=username).first()

    if not user or not check_password_hash(user.password, password):
        flash("Either the username or password is incorrect. Please try again.")
        return redirect(url_for("login"))

    login_user(user, remember=remember)

    return redirect(url_for("dashboard"))


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("home"))


@app.route('/dashboard')
@login_required
def dashboard():
    images = {}
    for i in current_user.images:
        link = get_from_aws(i[0])
        images[i[1]] = [link, i[2], i[0]]
    return render_template('dashboard.html', name=current_user.username,
                           contents=images)


@app.route('/upload')
@login_required
def upload_page():
    return render_template('image_selector.html')


@app.route('/upload', methods=['POST'])
@login_required
def upload():
    data = request.files.getlist('img')
    access = "private"
    if request.form.get('access_public') is not None:
        access = "public"
    error_check = False

    for i in data:
        selected = aws_upload(i, access)
        if not selected:
            error_check = True

    if error_check:
        flash("One or more images have not been uploaded successfully.")
    else:
        flash("All images uploaded successfully.")

    return redirect(url_for('upload'))


@app.route('/get_public_images')
@login_required
def get_public_images():
    images = []
    for i in PublicImages.query.all():
        images.append(get_from_aws(i.image))
    return render_template("public_view.html", contents=images)


@login_required
def aws_upload(file, access):
    connection = boto3.client("s3", aws_access_key_id=access_key,
                              aws_secret_access_key=secret)
    object_key = current_user.username + str(current_user.id) + file.filename
    try:
        if access == "public":
            image = PublicImages(image=object_key)
            db.session.add(image)
        connection.upload_fileobj(file, aws_bucket, object_key)
        current_user.images = current_user.images + [[object_key,
                                                      file.filename, access]]
        db.session.commit()
        return True
    except Exception as exp:
        print("Something Happened: ", exp)
        return False


@login_required
def get_from_aws(object_key):
    connection = boto3.client("s3", aws_access_key_id=access_key,
                              aws_secret_access_key=secret)
    try:
        signed_url = connection.generate_presigned_url('get_object',
                                                       Params={'Bucket':
                                                                   aws_bucket,
                                                               'Key':
                                                                   object_key},
                                                       ExpiresIn=60)
        return signed_url
    except Exception as exp:
        pass


@app.route('/delete_image/<object_key>')
@login_required
def delete_img(object_key):
    connection = boto3.client("s3", aws_access_key_id=access_key,
                              aws_secret_access_key=secret)
    try:
        connection.delete_object(Bucket=aws_bucket, Key=object_key)
    except Exception as exp:
        flash("Something went wrong. Please try again later.")

    PublicImages.query.filter_by(image=object_key).delete()

    for i in current_user.images:
        if i[0] == object_key:
            lst_copy = current_user.images.copy()
            lst_copy.remove(i)
            current_user.images = lst_copy
            flash("Image Deleted Successfully.")

    db.session.commit()
    return redirect(url_for("dashboard"))


if __name__ == '__main__':
    app.run()
