
The Testing.md file provides a comprehensive overview of the tests conducted on the Roadster Expert website. It covers code validation, accessibility, performance, testing on various devices, browser compatibility, testing of user stories, and improvements. Each section describes the tools used, any issues identified (if applicable), and the corresponding test results.
You can find [here](README.md) main readme file.

## Content

*   [Pep8 Validation](#pep8-validation)
*   [Google Lighthouse](#google-lighthouse)
*   [Html Validation](#html-validation)
*   [JS Validator](#js-validator)
*   [CSS Validator](#css-validator)
*   [Error Pages](#error-pages)
*   [Bugs](#bugs)

## Pep8 Validation

The PEP8 compliance check for all .py files within the Experiences and Vehicles applications has been successfully completed without any errors.

[Content](#content)

## Google Lighthouse

![Google Lighthouse Result](/assets/validators/light_mobile.jpg "Google Lighthouse Result")

The image above displays the mobile device result of Google Lighthouse.

[Content](#content)

## Html Validation

![Home](/assets/validators/html/home.png "Home")

![All Vehicle](/assets/validators/html/categories.png "All Vehicle")

![Category Cabrio](/assets/validators/html/category_cabrio.png "Category Cabrio")

![Category Coupe](/assets/validators/html/category_coupe.png "Category Coupe")

![Category Pickup](/assets/validators/html/category_pickup.png "Category Pickup")

![Category Targa](/assets/validators/html/category_targa.png "Category Targa")

![About](/assets/validators/html/about.jpg "About")

![Contact](/assets/validators/html/contact.png "Contact")

![Experiences](/assets/validators/html/experiences.png "Experiences")

![Create Experience](/assets/validators/html/create_experience.png "Create Experience")

![My Experience](/assets/validators/html/my_experience.png "My Experience")

![Experience Detail](/assets/validators/html/experience_detail.png "Experience Detail")

![Profile](/assets/validators/html/profile.png "Profile")

![Sign Up](/assets/validators/html/signup.png "Sign Up")

![Sign In](/assets/validators/html/login.png "Sign In")

![Sign Out](/assets/validators/html/logout.png "Sign Out")

[Content](#content)

## JS Validator 

![Email JS](/assets/validators/sendMailJs.png "Email JS")

![Roadster JS](/assets/validators/roadster_js.png "Roadster JS")

[Content](#content)

## CSS Validator

![Roadster CSS](/assets/validators/css_validator.png "Roadster CSS")

[Content](#content)

## Error Pages

I have included pages to handle HTTP errors with status codes 400 and 505 in my project. However, for requests that do not match URL patterns, my 404 page is displayed. This is a standard response provided when users request pages with URLs that do not exist or are incorrect. It allows users to notice missing or incorrect URLs and be directed to the correct page.

In case of an HTTP 500 error, the server encounters an internal error and is unable to handle the request properly. This could occur due to various reasons such as bugs in the server-side code, database connection issues, or insufficient server resources. In such situations, users may encounter a generic error page indicating that something has gone wrong on the server side.

[404 Pages](README.md#404-page) | [500Pages](README.md#500-page)

[Content](#content)

## Bugs

### Fixed Bugs

#### All Vehicle Menu

The menu categorizing vehicles. When I started the project, there was no issue because only the home page was set up, and the category information was included in the context. However, I noticed that the menu was missing when I added About and Contact pages. After some research, I came across this article in the source [Context Processor](https://docs.djangoproject.com/en/5.0/ref/templates/api/). Now the menu works perfectly fine; when you add a new category, you can see it in the All Vehicle menu.

#### Profile Menu

My esteemed mentor, Mr. Antonio Rodriguez, informed me during testing that there was an issue with the Profile screen, specifically reporting a "No Profile" error. As a result of my research, I understood that I needed to implement the Signal structure available in Django and establish this relationship between User and Profile. After establishing this relationship, everything went smoothly!

[Content](#content)