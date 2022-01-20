# cloud-image-repository
 
Using Python, Flask and Amazon Web Services, I have developed a cloud based Image Repository.

Since the code requires AWS secret keys (which I can't publish on git for security reasons) I have published the working applicating here: 

https://ratantej.pythonanywhere.com/ 


# Key Features

- The app is developed on Python and Flask
- It is entirely run on cloud using AWS S3, and AWS RDS
- Access Control (User login, and sessions)
- With this image repository a user can upload, store, and view images. 
- Users can upload multiple images at once.
- The User can also delete images
- The app boasts a public image library and private one. The user decides at the time of upload if they want their upload to be visible to all users or just them. 
- All user account passwords are encrypted and hashed using Werkzeug
- Used Flask-login to authenticate, manage and create user sessions 


# How to use the App

### Step 1: Go to https://ratantej.pythonanywhere.com/  - This is where the app is hosted. 

Your are welcomed with an homepage. Click on get started to create an account or click on sign up in the top right corner.

<img width="1851" alt="Screen Shot 2022-01-19 at 11 13 32 PM" src="https://user-images.githubusercontent.com/70780442/150272658-106633ff-d3e2-45c4-90d2-4b896da96201.png">

### Step 2: Create a new user account with an email, username, and set a password. And then Log in! 

<img width="1851" alt="Screen Shot 2022-01-19 at 11 21 28 PM" src="https://user-images.githubusercontent.com/70780442/150272868-3983baaa-cc96-4efb-bbe4-d529b589b5ff.png">

### Step 3: After you log in, you can see your dashboard. At the beginning its empty, but you can start uploading photos by clicking on Upload in the top right corner. Dashboard is where you will be able to view all your uploads and manage them.

<img width="1851" alt="Screen Shot 2022-01-19 at 11 32 41 PM" src="https://user-images.githubusercontent.com/70780442/150273910-0bcb07cf-0f96-4ebe-9f60-e0bbe12827ae.png">

### Step 4: Uploading your first image. Select an image or images. You can select multiple images at once. Then select whether you would like to make the upload public or not. If this option is selected, then the images will be visible to the other users as well under the Public Images Menu. Similarly you can visit the Public Images Menu to view images available to the public by other users on the repository. Remember: Visibility cannot be changed after upload

<img width="1851" alt="Screen Shot 2022-01-19 at 11 37 09 PM" src="https://user-images.githubusercontent.com/70780442/150274326-e0dff8a7-98ec-4076-ab4e-76e14cd929f5.png">

### Step 5: After Uploading, you can click on show images to go back to dashboard to view all your uploads and manage them or click on the dashboard menu option from the nav bar. In the dashboard, you can view all your uploads. You can even delete a file by clicking the delete button beside it. You can also download the image by clicking on the image link

<img width="1851" alt="Screen Shot 2022-01-19 at 11 40 48 PM" src="https://user-images.githubusercontent.com/70780442/150274692-874d14e4-1858-4c84-af5f-50f87c256c4b.png">

### Step 6: View All Public Uploads by clicking on Public Images Menu option. Here you can view all publicly available images on repository. You can download any image here by clicking on it but you cannot delete other users images (there is an access control in place - which is the dashboard)

![Screen Shot 2022-01-19 at 11 47 00 PM](https://user-images.githubusercontent.com/70780442/150275317-5c41cac3-81a4-4672-bb6c-741264996e92.jpg)

### Step 7: Once you're done, don't forget to logout in the top right hand corner!!

# Backend (AWS S3 and RDS)

On the back end, I'm using S3 and RDS to support this entire app. The S3 has a bucket that holds all the images. And RDS has a Postgresql databse that hold all the user data such as login credentials and data related to what images belong to that user. 

<img width="1802" alt="Screen Shot 2022-01-19 at 11 52 25 PM" src="https://user-images.githubusercontent.com/70780442/150275729-74861073-8db2-4db2-8bcf-eaa0d4338aa1.png">

<img width="1802" alt="Screen Shot 2022-01-19 at 11 53 39 PM" src="https://user-images.githubusercontent.com/70780442/150275839-ac05a10e-9645-4698-962d-5fb4a1077ebc.png">


