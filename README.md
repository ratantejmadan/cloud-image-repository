# cloud-image-repository
 
Using Python, Flask and Aamazon Web Services, I have developed a cloud based Imagae Repository.

Since the code requires AWS secret keys (which I can't publish on git for security reasons) I have published the working applicating here: 

https://ratantej.pythonanywhere.com/ 


# Key Fetaures

- The app is developed on Python and Flask
- It is entirely run on cloud using AWS S3, and AWS RDS
- Access Control (User login, and sessions)
- With this image repository a user can upload, store, and view images. 
- Users can upload multiple images at once
- The app boasts a public image library and private one. The user decideds at the time of upload if they want their upload to be visible to all users or just them. 
- All user account passowrds are encrypted and hashed using Werkzeug
- Used Flask-login to authenticate, manage and create user sessions 


# How to use the App

### Step 1: Go to https://ratantej.pythonanywhere.com/  - This is where the app is hosted. 

Your are welcomed with an homepage. Click on get started to create an account or click on sign up in the top right corner.

<img width="1851" alt="Screen Shot 2022-01-19 at 11 13 32 PM" src="https://user-images.githubusercontent.com/70780442/150272658-106633ff-d3e2-45c4-90d2-4b896da96201.png">

### Step 2: Create a new user account with an email, username, and set a password. And then Log in! 

<img width="1851" alt="Screen Shot 2022-01-19 at 11 21 28 PM" src="https://user-images.githubusercontent.com/70780442/150272868-3983baaa-cc96-4efb-bbe4-d529b589b5ff.png">

### Step 3: After you log in, you can see your dashbord. At the beginning its empty, but you can start uploading photos by clicking on Upload in the top right corner. 

<img width="1851" alt="Screen Shot 2022-01-19 at 11 32 41 PM" src="https://user-images.githubusercontent.com/70780442/150273910-0bcb07cf-0f96-4ebe-9f60-e0bbe12827ae.png">

### Step 4: Uploading your first image. Select an image or images. You can select multiple images at once. Then select whether you would like to make the upload public or not. If this option is selected, then the images will be visible to the other users as well under the Public Images Menu. Similarly you can visit the Public Images Menu to view images avaiable to the public by other users on the repository. 

<img width="1851" alt="Screen Shot 2022-01-19 at 11 37 09 PM" src="https://user-images.githubusercontent.com/70780442/150274326-e0dff8a7-98ec-4076-ab4e-76e14cd929f5.png">




