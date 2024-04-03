# Roadster Expert - Introduction

Roadster Expert website is a Full Stack web application built on the Django Framework using the Python language as its foundation. The main purpose of this site is to provide a platform where users can share their experiences, opinions, or expertise regarding Roadster-type vehicles, either with experts or among themselves. Registered users can comment on and like posts, as well as share their experiences with the vehicles they have had the opportunity to use. Non-registered users can access the content and benefit from the information available on the site.

You can find my web site [Roadster Expert](https://roadster-expert-07714854e0e0.herokuapp.com/).

![Roadster Expert Mobile Test Screen](/assets/mobile_test.jpg "Roadster Expert All Devices")

# Content Table


+ [Roadster Expert - Introduction](#roadster-expert---introduction)
+ [User Experience - UX](#user-experience---ux)
   + [User Stories](#user-stories)
   + [Agile Methodology](#agile-methodology)
   + [The Scope](#the-scope)
      + [Main Site Goals](#main-site-goals)
   + [Design](#design)
      + [Colours](#colours)
      + [Typography](#typography)
      + [Imagery](#imagery)
      + [Wireframes](#wireframes)
   + [Database Diagram](#database-diagram)
   + [Features](#features)
      + [Home Page](#home-page)
      + [All Categories](#all-categories)
      + [Blank Category](#blank-category)
      + [A Category](#a-category)
      + [Vehicle Detail](#vehicle-detail)
      + [All Experiences](#all-experiences)
      + [Create Experience](#create-experience)
      + [Experience Detail](#experience-detail)
      + [Search](#search)
      + [About](#about)
      + [Contact](#contact)
      + [Profile](#profile)
      + [Navbar](#navbar)
      + [Sign In](#sign-in)
      + [Sign Out](#sign-out)
      + [Sign Up](#sign-up)
      + [404 Page](#404-page)
      + [500 Page](#500-page)
   + [Messages](#messages-and-interaction-with-users)
      + [SignUp](#sign-up-message)
      + [Sign In](#sign-in-message)
      + [Sign Out](#sign-out-message)
      + [Profile Update](#profile-update-message)
      + [Like Post](#like-post-message)
      + [Unlike Post](#unlike-post-message)
      + [Comment Post](#comment-post-message)
      + [Edit Comment](#edit-comment-message)
      + [Delete Comment](#delete-comment-message)
      + [Email Sent](#email-sent---success-message)
      + [Create Experience](#create-experience-message)
      + [Update Experience](#update-experience-message)
      + [Delete Experience](#delete-experience-message)
   + [Admin Screen](#admin-screen)
      + [Future Features](#future-features)
   + [Technologies Used](#technologies-used)
      + [Languages Used](#languages-used)
         + [Django Packages](#django-packages)
      + [Framework - Libraries - Programs Used](#framework-libraries-programs-used)
      + [Testing](#testing)
   + [Creating the Django app](#creating-the-django-app)
   + [Deployment of this Project](#deployment-of-this-project)
   + [Final Deployment](#final-deployment)
   + [Forking this Project](#forking-this-project)
   + [Cloning this Project](#cloning-this-project)
   + [Credits](#credits)
      + [Content](#content)
   + [Special Thanks](#special-thanks)




# User Experience - UX

## User Stories

+ As a website user, I can:

1. Easily navigate around the site. 
2. View a list of vehicles and select a vehicle detail to read.
3. Search for a specific vehicle.
4. Open a post to read the details.
5. Create an account to get members features.
6. View the number of likes on a post.
7. View comments on a post.

+ As logged in website user, I can:

1. Like and unlike vehicles.
2. Comment on vehicles.
3. Delete or edit my previous comments.
4. Update my profile informations.
5. Share my driving experiences.
6. Edit or delete my previously experience.
7. Logout from the website.

+ As a website superuser, I can:

1. Create and publish a new Category / Brand / Model / Vehicle.
2. Create draft vehicle posts that can be reviewed and finalised later.
3. Create/Delete a new user, categories, brand, model, vehicle, experiences.
4. Approve user's comments.
5. Delete user's experiences that was posted previously.
6. Change the website permissions for a user.

[Content Table](#content-table)

## Agile Methodology
All the features and development of this project were overseen through GitHub, where you can find the [Projects](https://github.com/users/mdurmus/projects/6) section.

[Content Table](#content-table)

### The Scope

#### Main Site Goals

+ To provide users with a good experience when using the website.
+ To provide users with a visually pleasing website that is intuitive to use and easy to navigate.
+ To provide a website with a clear purpose.
+ To provide role-based permissions that allows user to interact with the website.

[Content Table](#content-table)

## Design

#### Colours

![Roadster Color Palette](/assets/roadster_color_palette.jpg "Roadster Color Palette")

[Content Table](#content-table)

I tried to benefit from approaches that describe the language of colors in my color selection.

[Content Table](#content-table)

#### Typography

I used the 'Montserrat' font obtained from Google Fonts throughout my entire website.

[Content Table](#content-table)

#### Imagery

The images have been selected to be as relevant as possible to the content. However, users can also add their own images.

[Content Table](#content-table)

#### Wireframes

I have drawn a few wireframes to get a close idea of what Wesbite will look like, but there may be some differences because I drew them before I created my project.

![Home Page](/assets/wireframes/home.png "Roadster Expert Home")

![Roadster Expert Vehicles](/assets/wireframes/vehicles.png "Roadster Expert Vehicles")

![Roadster Expert About](/assets/wireframes/about.png "Roadster Expert About")

![Roadster Expert Contact](/assets/wireframes/contact.png "Roadster Expert Contact")

![Roadster Expert Search](/assets/wireframes/search.png "Roadster Expert Search")

[Content Table](#content-table)

## Database Diagram

![Roadster Expert Database Diagram](/assets/database.png "Roadster Expert Database Diagram")

[Content Table](#content-table)

## Features

I tried to share only the images related to the desktop view under this heading.

[Content Table](#content-table)

### Home Page

![Roadster Expert Home Page](/assets/pages/home.jpg "Roadster Expert Home Page")

On the homepage, we encounter a simple and elegant slider that greets us. Just below, we come across a paragraph explaining why you should work with Roadster Expert. Everything is changing so fast, and we wanted to keep you informed by adapting to this change on our homepage.

[Content Table](#content-table)


### All Categories)

![Roadster Expert All Categories](/assets/pages/allVehicles.jpg "Roadster Expert All Categories")

This is the page where all registered categories are listed, and you can select the ones you want to see the registered vehicles.

[Content Table](#content-table)

### Blank Category

![Roadster Expert Blank Category](/assets/pages/blankCategory.jpg "Roadster Expert Blank Category")

If the admin has created a category but hasn't added any vehicles into it, this is the page you will see. You can also notify us by writing an email on this page if you wish.

[Content Table](#content-table)

### A Category

![Roadster Expert A Category](/assets/pages/category.jpg "Roadster Expert A Category")

As you might expect, you're viewing a category where many vehicles have been saved by the admin. If there are more vehicle records than can fit on one page, Django's pagination technique will take you to the other vehicles.

[Content Table](#content-table)

### Vehicle Detail

![Roadster Expert Vehicle Detail](/assets/pages/vehicle_detail.jpg "Roadster Expert Vehicle Detail")

Firstly, we encounter a brief overview of the relevant vehicle. Then, we see a stunning image of the vehicle. We observe how many times registered users have liked this vehicle. Its technical specifications are summarized in a table, followed by detailed information about the vehicle. Towards the end of the page, you can see the comments made by registered users for this vehicle. If a registered user is logged in, they can edit or delete their own comment.

[Content Table](#content-table)

### All Experiences

![Roadster Expert All Experiences](/assets/pages/allExperiences.jpg "Roadster Expert All Experiences")

This is the page where registered users can list their experiences. A summary table appears with keywords such as username, brand, model and date.

[Content Table](#content-table)

### Create Experience

![Roadster Expert Create Experience](/assets/pages/createExp.jpg "Roadster Expert Create Experience")

This is the page where our registered users share their experiences.

[Content Table](#content-table)

### Experience Detail

![Roadster Expert Experience Detail](/assets/pages/experienceDetail.jpg "Roadster Expert Experience Detail")

A page where the indescribable but essential emotions are attempted to be defined. As another member of the club, you can connect with the kidi who experienced this and maybe chat or even experience it yourself.

[Content Table](#content-table)

### Search

![Roadster Expert Search](/assets/pages/search.jpg "Roadster Expert Search")

This is the page where we share search results based on the keywords entered by our users, matching the titles, models, and contents of the vehicles registered in our database.

[Content Table](#content-table)


### About

![Roadster Expert About](/assets/pages/about.jpg "Roadster Expert About")

This is the page where information about the establishment purpose of the Roadster Expert club and its members is presented.

[Content Table](#content-table)

### Contact

![Roadster Expert Contact](/assets/pages/contact.jpg "Roadster Expert Contact")

On this page, you can access the Roadster Expert club with a single click, or you can also send an email to the club by filling out the contact form. You can also track the process of sending this email in real-time using the snippet above.

[Content Table](#content-table)

### Profile

![Roadster Expert Profile](/assets/pages/profile.jpg "Roadster Expert Profile")

This is the page where registered users update their information.

[Content Table](#content-table)

### Navbar

![Roadster Expert Desktop Navbar](/assets/pages/navbarDesktop.jpg "Roadster Expert Desktop Navbar")
![Roadster Expert Mobile Navbar](/assets/pages/navbarMobile.jpg "Roadster Mobile Navbar")
![Roadster Expert User Navbar](/assets/pages/navbarUser.jpg "Roadster Expert User Navbar")
![Roadster Expert Vehicles Navbar](/assets/pages/navbarVehicles.jpg "Roadster Expert Vehicles Navbar")

[Content Table](#content-table)

### Sign In

![Roadster Expert Sign In](/assets/pages/signin.jpg "Roadster Expert Sign In")

[Content Table](#content-table)

### Sign Out

![Roadster Expert Sign Out](/assets/pages/signout.jpg "Roadster Expert Sign Out")

[Content Table](#content-table)

### Sign Up

![Roadster Expert Sign Up](/assets/pages/signup.jpg "Roadster Expert Sign Up")

[Content Table](#content-table)

### 404 Page

![Roadster Expert 404 Page](/assets/pages/404.jpg "Roadster Expert 404 Page")

[Content Table](#content-table)

### 500 Page

![Roadster Expert 500 Page](/assets/pages/500.jpg "Roadster Expert 500 Page")

[Content Table](#content-table)


## Messages and Interaction With Users

### Sign up Message

![Sign up](/assets/messages/signup.png "Sign up")
[Content Table](#content-table)

### Sign in Message

![Login](/assets/messages/signin.png "Login")
[Content Table](#content-table)

### Sign out Message

![Logout](/assets/messages/signout.png "Logout")
[Content Table](#content-table)

### Profile Update Message

![Profile Update](/assets/messages/profileUpdate.png "Profile Update")
[Content Table](#content-table)

### Like Post Message

![Like Post](/assets/messages/like.png "Like Post")
[Content Table](#content-table)

### Unlike Post Message

![Unlike Post](/assets/messages/unlike.png "Unlike Post")
[Content Table](#content-table)

### Comment Post Message

![Comment Post](/assets/messages/commentPost.png "Comment Post")
[Content Table](#content-table)

### Edit Comment Message

![Edit Comment](/assets/messages/editComment.png "Edit Comment")
[Content Table](#content-table)

### Delete Comment Message

![Delete Comment](/assets/messages/deleteComment.png "Delete Comment")
[Content Table](#content-table)

### Email Sent - Success Message

![Email Sent](/assets/messages/sendMail.png "Email Sent")
[Content Table](#content-table)

### Create Experience Message

![Create Experience](/assets/messages/create_experience.png "Create Experience")
[Content Table](#content-table)

### Update Experience Message

![Update Experience](/assets/messages/update_experience.png "Update Experience")
[Content Table](#content-table)

### Delete Experience Message

![Delete Experience](/assets/messages/delete_experience.png "Delete Experience")
![Delete Experience2](/assets/messages/delete_experience2.png "Delete Experience2")
[Content Table](#content-table)



## Admin Screen

![Roadster Expert Admin](/assets/pages/admin.jpg "Roadster Expert Admin")

On the Admin Panel, as an admin/superuser I have full access to CRUD functionality so I can view, create, edit and delete the following ones:

- Brand
- Model
- Categories
- Vehicles
- Comments
- Experience
- Profiles

As superuser I can also approve comments, experience, posts and change the status and give other permissions to the users.

[Content Table](#content-table)

### Future Features

I want to add a favorite feature where logged-in users can add their own vehicles to their favorite list, so that they can easily check their favorite vehicles anytime. Additionally, I can enable the share button on the experience-detail page to allow sharing in posts.

## Testing

   Testing detail [here](TEST.md)

[Content Table](#content-table)

# Technologies Used

## Languages Used

- [HTML5](https://en.wikipedia.org/wiki/HTML "Html5 Wikipedia")

- [CSS3](https://en.wikipedia.org/wiki/CSS "CSS Wikipedia")

- [Javascript](https://www.javascript.com "Javascript")

- [Django](https://www.djangoproject.com "Django Official")

- [Python](https://www.python.org "Python Offical")

- [Duck Duck Go](https://duckduckgo.com)

[Content Table](#content-table)

### Django Packages

- [Gunicorn](https://gunicorn.org/)
   As the sever for Heroku

- [Cloudinary](https://cloudinary.com/)
   Was used to host the static files and media

- [Dj_database_url](https://pypi.org/project/dj-database-url/) 
   To parse the database URL from the environment variables in Heroku

- [Psycopg2](https://pypi.org/project/psycopg2/)
   As an adaptor for Python and PostgreSQL databases

- [Summernote](https://summernote.org/)
   As a text editor

- [Allauth](https://django-allauth.readthedocs.io/en/latest/installation.html)
   For authentication, registration, account management

- [Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/)
   To style the forms

## Framework - Libraries - Programs

- [Bootstrap](https://getbootstrap.com/)
   Was used to style the website, add responsiveness and interactivity

- [Jquery](https://jquery.com/)
   All the scripts were written using jquery library

- [Git](https://git-scm.com/)
   Git was used for version control by utilizing the Gitpod terminal to commit to Git and push to GitHub

- [GitHub](https://github.com/)
   GitHub is used to store the project's code after being pushed from Git

- [Heroku](https://id.heroku.com/)
   Heroku was used to deploy the live project

- [PostgreSQL](https://www.postgresql.org/)
   Database used through heroku.

- [VSCode](https://code.visualstudio.com/)
   VSCode was used to create and edit the website

- [Lucidchart](https://lucid.app/)
   Lucidchart was used to create the database diagram

- [PEP8](https://pep8ci.herokuapp.com/)
   PEP8CI was used to validate all the Python code

- [W3C - HTML](https://validator.w3.org/)
   W3C- HTML was used to validate all the HTML code

- [W3C - CSS](https://jigsaw.w3.org/css-validator/)
   W3C - CSS was used to validate the CSS code

- [Fontawesome](https://fontawesome.com/)
   To add icons to the website

- [Google Chrome Dev Tools](https://developer.chrome.com/docs/devtools/)
   To check App responsiveness and debugging

- [Emailjs](https://www.emailjs.com/)
   To send emails from the contact form

# Creating the Django app

+ Go to the Code Institute Gitpod Full Template Template
+ Click on Use This Template
+ Once the template is available in your repository click on Gitpod
+ When the image for the template and the Gitpod are ready open a new terminal to start a new Django App
+ Install Django and gunicorn: pip3 install django gunicorn
+ Install supporting database libraries dj_database_url and psycopg2 library: pip3 install dj_database_url psycopg2
+ Create file for requirements: in the terminal window type pip freeze --local > requirements.txt
+ Create project: in the terminal window type django-admin startproject your_project_name
+ Create app: in the terminal window type python3 manage.py startapp your_app_name
+ Add app to the list of installed apps in settings.py file: you_app_name
+ Migrate changes: in the terminal window type python3 manage.py migrate
+ Run the server to test if the app is installed, in the terminal window type python3 manage.py runserver
+ If the app has been installed correctly the window will display The install worked successfully! Congratulations!

[Content Table](#content-table)


# Deployment of this Project

+ Log in to [Heroku](https://www.heroku.com) or create an account
+ On the main page click the button labelled New in the top right corner and from the drop-down menu select Create New App
+ You must enter a unique app name
+ Next select your region
+ Click on the Create App button
+ Click in resources and select Heroku Postgres database
+ Click Reveal Config Vars and add a new record with SECRET_KEY
+ Click Reveal Config Vars and add a new record with the CLOUDINARY_URL
+ Click Reveal Config Vars and add a new record with the `DISABLE_COLLECTSTATIC = 1`
+ The next page is the project’s Deploy Tab. Click on the Settings Tab and scroll down to Config Vars
+ Next, scroll down to the Buildpack section click Add Buildpack select python and click Save Changes
+ Scroll to the top of the page and choose the Deploy tab
+ Select Github as the deployment method
+ Confirm you want to connect to GitHub
+ Search for the repository name and click the connect button
+ Scroll to the bottom of the deploy page and select the preferred deployment type
+ Click either Enable Automatic Deploys for automatic deployment when you push updates to Github

[Content Table](#content-table)

# Final Deployment

+ Create a runtime.txt **python-3.8.13**
+ Create a Procfile `web: gunicorn your_project_name.wsgi`
+ When development is complete change the debug setting to: `DEBUG = False` in settings.py
+ In this project the summernote editor was used so for this to work in Heroku add: `X_FRAME_OPTIONS = SAMEORIGIN` to settings.py.
+ In Heroku settings, delete the config vars for `DISABLE_COLLECTSTATIC = 1`

[Content Table](#content-table)

# Forking this Project

+ Open [GitHub](https://www.github.com)
+ Find the 'Fork' button at the top right of the page
+ Once you click the button the fork will be in your repository

[Content Table](#content-table)

# Cloning this Project

+ Open [GitHub](https://www.github.com)
+ You will be provided with three options to choose from, HTTPS, SSH or + GitHub CLI, click the clipboard icon in order to copy the URL
+ Once you click the button the fork will be in your repository
+ Open a new terminal
+ Change the current working directory to the location that you want the cloned directory
+ Type 'git clone' and paste the URL copied in step 3
+ Press 'Enter' and the project is cloned

# Credits

## Content

+ All text generated from Chat GPT

+ All images from [Adobe Stock](https://www.adobestock.com)

+ Colors and logo files that i downloaded for free from the internet.

# Special Thanks

I would like to express my endless gratitude to [soukasamadi](https://github.com/soukasamadi/), a valued member of Code Institute, whose significant contributions have been instrumental in the preparation of this project.

I would also like to thank my mentor, Antonio Rodriguez, for their valuable insights.