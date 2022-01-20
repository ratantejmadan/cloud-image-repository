# cloud-image-repository
 
Using Python, Flask and Aamazon Web Services, I have developed a cloud based Imagae Repository.

Since the code requires AWS secret keys (which I can't publish on git for security reasons) I have published the working applicating here: 

https://ratantej.pythonanywhere.com/ 


# Key Fetaures

- The app is developed on Python and Flask
- It is entirely run on cloud using AWS S3, and AWS RDS
- Access Control (User login, and sessions)
- With this image repository a user can upload, store, and view images. 
- The app boasts a public image library and private one. The user decideds at the time of upload if they want their upload to be visible to all users or just them. 
- All user account passowrds are encrypted and hashed using Werkzeug
- Used Flask-login to authenticate, manage and create user sessions 


# How to use the App

### Step 1: Go to https://ratantej.pythonanywhere.com/  - This is where the app is hosted. 

Your are welcomed with an homepage. Click on get started to create an account or click on sign up in the top right corner.

<img width="1851" alt="Screen Shot 2022-01-19 at 11 13 32 PM" src="https://user-images.githubusercontent.com/70780442/150272658-106633ff-d3e2-45c4-90d2-4b896da96201.png">

