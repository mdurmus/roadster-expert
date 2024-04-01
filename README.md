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
        + [Admin Screen](#admin-screen)
            + [Future Features](#future-features)
        + [Technologies Used](#technologies-used)
            + [Languages Used](#languages-used)



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
All the features and development of this project were overseen through GitHub, where you can find the [Projects](https://github.com/users/mdurmus/projects/4) section.

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

![Roadster Expert Navbar](/assets/pages/navbarDesktop.jpg "Roadster Expert Navbar")
![Roadster Expert Navbar](/assets/pages/navbarMobile.jpg "Roadster Expert Navbar")
![Roadster Expert Navbar](/assets/pages/navbarUser.jpg "Roadster Expert Navbar")
![Roadster Expert Navbar](/assets/pages/navbarVehicles.jpg "Roadster Expert Navbar")

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


## Admin Screen

here admin screen

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

I would like to add a favorite feature where logged-in users can add their own vehicles to their favorite list, so that they can easily check their favorite vehicles anytime.

## Technologies Used

### Languages Used

["HTML5"](https://en.wikipedia.org/wiki/HTML "Html5 Wikipedia")
[CSS3](https://en.wikipedia.org/wiki/CSS "CSS Wikipedia")
[Javascript](https://www.javascript.com "Javascript")
[Django](https://www.djangoproject.com "Django Official")
[Python](https://www.python.org "Python Offical")
[Duck Duck Go](https://duckduckgo.com)

[Content Table](#content-table)

## Django Packages

