# Wordsmith

![AmIResponsive image of Wordmith](assets/screenshots/responsive-wordsmith.png)

## Introduction
Wordsmith is a website built in Django using Python, JavaScript, CSS and HTML. It allows the user to share in the love of writing stories by giving them the opportunity to create their own short stories for others to read as well as read other short stories other users have posted.

They can give their story a heading, a blurb (content on the back of a book), a book cover and of course the content. You can edit your own stories as well as delete them if you wish.

[View the live website on Heroku](https://wordsmith-fafcef7f3870.herokuapp.com/)

## Table of Contents
* [User Experience Design (UX)](#UX)
    * [The Strategy Plane](#The-Strategy-Plane)
        * [Site Goals](#Site-Goals)
        * [Epics](#Epics)
        * [User Stories](#User-Stories)
    * [The Scope Plane](#The-Scope-Plane)
    * [The Structure Plane](#The-Structure-Plane)
        * [Opportunities](#Opportunities)
    * [The Skeleton Plane](#The-Skeleton-Plane)
        * [Wireframes](#Wireframe-mockups)
        * [Database Schema](#Database-Schema)
    * [The Surface Plane](#The-Surface-Plane)
* [Features](#features)
* [Future Enhancements](#future-enhancements)
* [Technologies Used](#technologies-used)
* [Testing](#testing)
* [Deployment](#deployment)
* [Credits](#credits)

## UX
### The Strategy Plane
*  Wordsmith is intended to be a site for users to create their own short stories for them to express themselves and share them for others to read. The user experience and design is to imply simplicity so that the users are not overloaded with information and get to the core of just creating, reading and enjoying the experience Wordsmith has to offer.

##### The Sites Ideal User
* A creative writer looking to share their own stories
* Someone who wants to enjoy reading short stories 
* A creative writer who wants to enjoy the art od story creation

#### Site Goals

* To provide users a place to create and edit their own stories for others to read
* To provide users a place to read other short stories

#### Epics

4 Epics were created which were then further developed into 18 User Stories. The details on each epic, along with the user stories linked to each one can be found in the project kanban board [here](https://github.com/users/SerJosh/projects/6/views/1)


1. Initial Django Setup [#1](https://github.com/SerJosh/wordsmith/issues/1)
2. User Account [#4](https://github.com/SerJosh/wordsmith/issues/4)
3. User Short Stories [#14](https://github.com/SerJosh/wordsmith/issues/14)
4. Enhancing website design [#19](https://github.com/SerJosh/wordsmith/issues/19)

### User Stories
From the Epics, 18 User stories were developed. Each story was assigned a classification of Must-have, Should-have, Could-have or Wont-have. Each story was also assigned user story points, based on my best estimation for the time/difficulty of completing each story. A combination of being new to story estimation, inexperience with Django and time constraints during development left me completing [find out story points] story points from the initial total of [find out story points]. In an attempt to understand my scope, I did not create a vast amout of user stories initially but created essential must have stories to work on and after the completion of them developed some should-have or lower user stories to work with. The full list of User Stories, seperated by those completed and those pushed to a future release is available on the project [kanban board](https://github.com/users/SerJosh/projects/6/views/1).

1. Initial Django setup
	* USER STORY: Django Setup [#2](https://github.com/SerJosh/wordsmith/issues/2) As a Developer, I want to set up Django and install the supporting libraries needed, so that I am ready to start development
	* USER STORY: Early Deployment to Heroku [#3](https://github.com/SerJosh/wordsmith/issues/3)
	
2. User Account
	* USER STORY: Create a User Account [#5](https://github.com/SerJosh/wordsmith/issues/5)
	* USER STORY: Users must confirm their email [#6](https://github.com/SerJosh/wordsmith/issues/6)
	* USER STORY: Users can reset their password [#7](https://github.com/SerJosh/wordsmith/issues/7)
	* USER STORY: Users can view their profile [#8](https://github.com/SerJosh/wordsmith/issues/8), As a User I can see the details in my user profile so that I can see the information of my user account
	* 
	* 

3.  USER Short Stories
	* 
	* 

4.  Enhancing website design
	* 
	* 
	* 
	*  




### The Scope Plane

**Features planned:**
* 
* 
* 


### The Structure Plane

User Story:

> [#2](https://github.com/SerJosh/wordsmith/issues/2) Django Setup - As a Developer, I want to set up Django and install the supporting libraries needed, so that I am ready to start development

Implementation:
* Install Django
* Install dj_database_url psycopg2
* Create a requirements.txt file
* Create the Django project – called wordsmith
* Create the first app, called stories and add it to the installed apps in the settings.py
* Create new instance in Postgres SQL and connect database to code

User Story:

> [#3](https://github.com/SerJosh/wordsmith/issues/3) Early Deployment to Heroku  - As a Developer, I want to deploy the app to Heroku, so that I can confirm everything works before development of the site.

Implementation:
* Update code for deployment
* Create new Heroku app
* Connect Heroku to the PostgreSQL database
* Implement and add Secret Key to project and Heroku config var

User Story:

> 

Acceptance Criteria:
* Given 
* Given that 
* Given that 
* Given that 

Implementation:
* 
* 

User Story:

> 

Acceptance Criteria:
* Given 
* Given that 
* Given that 
* Given that 

Implementation:
* 
* 

User Story:

> 

Acceptance Criteria:
* Given 
* Given that 
* Given that 
* Given that 

Implementation:
* 
* 

User Story:

> 

Acceptance Criteria:
* Given 
* Given that 
* Given that 
* Given that 

Implementation:
* 
* 

User Story:

> 

Acceptance Criteria:
* Given 
* Given that 
* Given that 
* Given that 

Implementation:
* 
* 

User Story:

> 

Acceptance Criteria:
* Given 
* Given that 
* Given that 
* Given that 

Implementation:
* 
* 

User Story:

> 

Acceptance Criteria:
* Given 
* Given that 
* Given that 
* Given that 

Implementation:
* 
* 

User Story:

> 

Acceptance Criteria:
* Given 
* Given that 
* Given that 
* Given that 

Implementation:
* 
* 

User Story:

> 

Acceptance Criteria:
* Given 
* Given that 
* Given that 
* Given that 

Implementation:
* 
* 

User Story:

> 

Acceptance Criteria:
* Given 
* Given that 
* Given that 
* Given that 

Implementation:
* 
* 

User Story:

> 

Acceptance Criteria:
* Given 
* Given that 
* Given that 
* Given that 

Implementation:
* 
* 

User Story:

> 

Acceptance Criteria:
* Given 
* Given that 
* Given that 
* Given that 

Implementation:
* 
* 

User Story:

> 

Acceptance Criteria:
* Given 
* Given that 
* Given that 
* Given that 

Implementation:
* 
* 

User Story:

> 

Acceptance Criteria:
* Given 
* Given that 
* Given that 
* Given that 

Implementation:
* 
* 

User Story:

> 

Acceptance Criteria:
* Given 
* Given that 
* Given that 
* Given that 

Implementation:
* 
* 

User Story:

> 

Acceptance Criteria:
* Given 
* Given that 
* Given that 
* Given that 

Implementation:
* 
* 

#### Opportunities

Arising from user stories
| Opportunities | Importance | Viability / Feasibility
| ------ | :------: | :------: |
| ** Provide users the ability to create an account ** | 5 | 5 |
| ** Provide users the ability to create recipes ** | 5 | 5 |
| ** Provide users the ability to edit recipes ** | 5 | 5 |
| ** Provide users the ability to view recipes ** | 5 | 5 |
| ** Provide users the ability to delete recipes ** | 5 | 5 |
| ** Provide users the ability to edit their account ** | 5 | 5 |
| ** Provide users the ability to view other accounts ** | 5 | 5 |
| ** Provide users the ability to delete their account ** | 5 | 5 |
| ** Provide users the ability to change the colour scheme ** | 2 | 5 |
| ** Provide users the ability to save a recipe ** | 3 | 5 |
| ** Provide users the ability to rate a recipe ** | 3 | 5 |
| ** Provide users the ability to access the site on any device ** | 5 | 5 |
| ** Provide users the ability to search the site for recipes ** | 4 | 5 |

### The Skeleton Plane
#### Wireframe mock-ups

Home page: The home page provides the user with a clear understanding as to the purpose of the site. There is a clear call to action for the user to search for a recipe with the inclusion of a search bar at the top of the home page. The welcome message is clearly visable to the user when they first arrive at the site regardless of the device they are using.

![Home Page Wireframe](/assets/wireframes/homepage-desktop.png)

Users have the ability to create recipes to share with other users. The emphasis of the design is to provide a clear recipe layout that can adapt to any size device. Clearly seperating general information, ingredients and steps.

![Recipe Detail Desktop Wireframe](/assets/wireframes/recipe-detail-desktop.png)

Users also have the ability to create a personal profile. From this profile users can access the recipes they have created and those that they have liked quickly and easily. They can also control the information they share with other users.

![User Profile Desktop Wireframe](/assets/wireframes/individual-profile-desktop.png)

Users will have the ability to search for recipes based on a search query of their choice. To aid in the discovery of different recipes, each recipe will be displayed in the form of a summary card from which the user can access the full recipe details.

![Recipe search page with results desktop wireframe](/assets/wireframes/recipe-search-desktop.png)

Users will have the ability to search for other users, so if there is a user who's recipes they like regularly, they can access their profile to find out more information about them.

![Profile search page with results desktop wireframe](/assets/wireframes/profiles-page-desktop.png)

Wireframes were also produced for each major page for both mobile and tablet devices. With the intention of the site being fully responsive so that no matter the device size the user is viewing the site on, it will display accordingly.

* [Home page mobile wireframe](/assets/wireframes/homepage-mobile.png)
* [Home page tablet wireframe](/assets/wireframes/homepage-tablet.png)
* [Recipe detail page mobile wireframe](/assets/wireframes/recipe-detail-mobile.png)
* [Recipe search page mobile wireframe](/assets/wireframes/recipe-search-mobile.png)
* [Recipe search page tablet wireframe](/assets/wireframes/recipe-search-tablet.png)
* [User profile search results page mobile wireframe](/assets/wireframes/profiles-page-mobile.png)
* [User profile search results page tablet wireframe](/assets/wireframes/profiles-page-tablet.png)

#### Database Schema

Several custom models were predicted to be required when building the site. The intention to utilise AllAuth for the user authentication system, which utilises the built in Django User Model removed the need to build a custom User model, however a custom User Profile was required. In order for the users to create Recipes a custom recipe model was required, which would be linked to the User Profile through using the profile as a foreign key. As each recipe could have a different number of ingredients or steps to it, it was decided to seperate out the ingredients and steps into their own model, and link them to the recipe through a foreign key. The database schema was planned using [DrawSQL app](https://drawsql.app/). Limitations of the app prevented labelling the field types correctly, it did not include the option to override the types available and did not include textarea, cloudinary fields or url fields. The models in the app reflect the true field choice.

![Database Schema Diagram](/assets/wireframes/database-scheme.png)

### The Surface Plane

#### Design

Once I was happy with the overall structure of the site, and the layout of the wireframes, I selected the colour scheme using the adobe colour selector. This was repeated for the darker colour scheme, I also referenced the google material design guidelines for the darker colour scheme. Both colour schemes were checked for colour contrast to ensure that the appropriate colours were used for a high level of colour contrast to maximise accessibility for users.

##### Typography 
Poppins a sans serif font was chosen for its clean clear design. It is important that the text of the recipes and the site are clear and easy for users to read, especially considering the nature of the site and that users might be reading the recipes whilst cooking.

##### Images
Several cartoon chef characters were accessed from [Vecteezy.com](https://www.vecteezy.com/members/heriyusuf/uploads). The artist Heriyusuf is responsible for the artwork for each cartoon chef. The artwork is available on a free license from [Vecteezy.com](https://www.vecteezy.com). 


## Features
#### Home page
A welcoming homepage was built to welcome the user to the site and clearly convey the sites purpose. The call to action for the user to search for recipes is at the top of the main page, with a large, hero like welcome message appearing just below. At the bottom of the page a clear comparison showing users the benefits of signing up to the site is displayed.

![Home Page](/assets/screenshots/homepage-light-desktop800.png)

#### Navigation Bar
The main navigation bar appears at the top of the page, clearly displaying the main navigational links users would require.

![Logged in User Nav Bar](/assets/screenshots/logged-in-navbar.png)

A secondary user menu is available to users who are logged into the site, users who are not logged in receive a login/register link in its place

![logged in user nave bar user menu open](/assets/screenshots/logged-in-navbar-user-menu-open.png)

The navigation bar and the user menu are fully responsive, adapting to narrower devices by appearing from the right hand side of the screen when the menu button is pressed.

![mobile user menu open](/assets/screenshots/mobile-user-menu-open.png)

#### Colour Mode Settings
Users have the ability to change the colour scheme in use on the site through a settings menu which opens a modal containing a toggle switch.

![mobile colour modal open](/assets/screenshots/mobile-color-modal-open.png)

#### Footer
A common footer is utilised through out the site to encourage users to visit the social media sites of the main site. They currently direct users to the generic social media sites, all external links open in a new tab.

![footer](/assets/screenshots/footer.png)

#### Recipe Search
Users have the ability to search the database of recipes against the recipe title and the author of the recipes username.

![Recipe search Desktop](/assets/screenshots/recipe-search-desktop.png)

#### Recipe Cards
Search results appear in the form of recipe summary cards. The cards show the user the title of the recipe, the featured image of the recipe, and the author of the recipe, if they have chosen to create a username. If the author has included a link to the recipe on Youtube, a little video icon displays. If the User has liked the recipe previously, and they are logged in when conducting the search, a little red thumbs up appears. If the user is logged in and they have added the recipe to their favourites list, a red heart appears on the recipe card. This allows the users to quickly identify the recipes they would like to look at in more detail.

##### Standard Recipe Card
![Standard Recipe Card](/assets/screenshots/standard-recipe-card.png)

##### Liked Recipe Card with video
![Liked Recipe card](/assets/screenshots/liked-recipe-summary-card.png)

##### Favourited Recipe Card
![Favourited Recipe Card](/assets/screenshots/favourited-recipe-card.png)

#### User Profile
Users have the ability to create a profile. If they choose not to complete the profile, the area they choose not to complete lets the user know what would appear in that section, it also informs them if other users can see the message or not. The user profile page provides the profile owner with quick access to edit and delete functionality.

![Owner Profile Page](/assets/screenshots/owner-profile-page.png)

Users can also access their own recipes, and the recipes they have liked from their profile page quickly and easily.

![Easy Access to own and liked recipes](/assets/screenshots/easy-access-to-own-liked-recipes.png)

#### Edit Profile Page
Users have the ability to edit their profiles on the site. The edit profile page is clearly laid out, and informs the user of the characters remaining for each field. The current profile image is displayed with the user having the ability to change the image.

![Edit profile page](/assets/screenshots/edit-profile-page.png)

#### Create/Edit Recipe Page
Users have the ability to create and edit their recipes. The create recipe and edit recipe page is clearly laid out, with the ingredients and steps sectioned off and individually editable/deletable.

##### Recipe Form
![Recipe Form](/assets/screenshots/recipe-form.png)

##### Ingredients Form
![Ingredients Form](/assets/screenshots/ingredient-form.png)

##### Steps Form
![Steps Form](/assets/screenshots/steps-form.png)

#### Access to Edit Recipe and Delete Recipe Functionality
Only the users that create the recipe can edit it or delete it. If the authorised user is the recipe author, then the edit recipe and delete recipe buttons will appear on the recipe detail page. The recipe like counter appears on the recipe card for recipes the user created, however it is not functional, and only displays the total number of likes that recipe has received.

##### Own recipe detail card
![Own recipe detail card](/assets/screenshots/recipe-detail-card-own-recipe.png)

##### Other users recipe detail card
![Other Users Recipe Detail Card](/assets/screenshots/recipe-detail-card.png)


## Future Enhancements
There are several items of functionality that I would like to add in the future. I have left the original user stories that were developed in the project kanban board as future enhancement opportunities.
The key areas I would like to add to the site in the future are:
* The ability for users to message other users
* The ability for users to comment on recipes
* The ability for users to login via social networks such as google or facebook

Some of the functionality above is provided by allauth which is already installed into the site, and therefore only has to be setup in order for it to function. Others would need to be developed completely.

## Testing

### Testing Strategy
I utilised a manual testing strategy for the development of the site. A full detailed breakdown of the testing procedures and methodology can be found in the testing.md file [here](TESTING.md).
Seperate to the functionality testing of the site, and the testing of the code, User Story tests were implemented to ensure that the acceptance criteria of the user stories listed above were met. The commit at which the functionality requirements for each user story were met is listed in the issues section of the repo. It was applied to each issue before it was closed and marked as completed.


#### Testing Overview

Testing was divided into different sections to ensure everything was tested individually with test cases developed for each area.

[Testing Schedule Overview](/assets/testing/test-schedule.pdf)

A full detailed breakdown of the testing procedures and methodology can be found in the testing.md file [here](TESTING.md)

#### Validator Testing
All code files were validated using suitable validators for the specific language. The full details can be found in the testing.md file.
All code passed the validation, with only code generated by other parties producing errors or warnings.
* Django built in code within the settings file produced five line length errors. 
* Bootstrap code produced 260 warnings in the CSS validation. 
* Fontawesome cdn produced 6 HTML validation errors relating to css variables within the cdn css code. 
* The HTMX library that is inserted into the HTML template by django produces a warning stating that the link does not need to have the javascript file type declared.

#### Notable Bugs

The use of CloudinaryFields for the images in the recipe and profile models does not enforce input validation to image file types. I could also not find anything related to enforcing the file types within the cloudinary documentation. This enabled users to attempt to upload non-image file types. To combat this issue, within the view that handles the form submission, I utilised a try, except statement that attempts to upload the file, but if the upload fails due to the file type error on the cloudinary servers, it gracefully handles the error and provides the user with an error message informing them what happened and why. This prevents users from breaking the functionality of the site, whilst still enabling them to correct the file they are trying to upload.

Development bugs: One major bug encountered during development still has me puzzled. I would repeatedly be unable to access the deployed site through Google Chrome on my home computer. Other users and I could access the deployed site on Google Chrome on other computers without issue, or in other browsers on the developement computer, however something on the computer used for development of the site would cause an issue repeatedly in chrome. This created a number of issues during the development of the site that had to be overcome.

No other bugs of note were found during development of the site. Several minor bugs were encountered due to small logic mistakes or scenario's unaccounted for, however these were found during the several rounds of testing and corrected. There are no known bugs left in the site.

#### Technologies Used

* Python
    * The following python modules were used on this project:
        * asgiref==3.5.0
        * certifi==2021.10.8
        * cffi==1.15.0
        * charset-normalizer==2.0.12
        * cloudinary==1.29.0
        * cryptography==36.0.1
        * defusedxml==0.7.1
        * dj-database-url==0.5.0
        * dj3-cloudinary-storage==0.0.6
        * Django==3.2
        * django-allauth==0.48.0
        * django-htmx==1.9.0
        * gunicorn==20.1.0
        * idna==3.3
        * oauthlib==3.2.0
        * psycopg2==2.9.3
        * pycparser==2.21
        * PyJWT==2.3.0
        * python3-openid==3.2.0
        * pytz==2021.3
        * requests==2.27.1
        * requests-oauthlib==1.3.1
        * six==1.16.0
        * sqlparse==0.4.2
        * urllib3==1.26.8

* Django
    * Django was used as the main python framework in the development of this project
    * Django AllAuth was utilised to provide enhanced user account management functionality.
* Heroku
    * Was used as the cloud based platform to deploy the site on
* Heroku PostgreSQL
    * Heroku PostgreSQL was used as the database for this project during development and in production.
* HTMX
    * HTMX is a JavaScript library that enables forms to be submitted and data to be retrieved from the backend without refreshing the entire page. It was used extensively for pages that included form submission such as the creation of the recipes where creating ingredients in another model, and creating steps in a third model was required. This package provided a simpler approach to using multiple formsets and custom JavaScript.
* JavaScript
    * Custom JavaScript was utilised to enable the colour scheme functionality, the mobile menu, the enabling and disabling of buttons on forms to prevent users inadvertantly causing errors when trying to submit multiple forms at the same time, and to display the current image in the form rather than a hyperlink to the image itself.
* Bootstrap 5.13
    * Bootstrap was used for general layout and spacing requirements for the site.
* Font Awesome
    * Was used for access to several icons for different sections where icons were appropriate.
* CSS
    * Custom css was written for a large number of areas on the site to implement custom styling and escape a bootstrap look and feel to the site.
* Jinja/Django Templating
    * Jinja/Django templating language was utilised to insert data from the database into the sites pages. It was also utilised to perform queries on different datasets.
* HTML
    * HTML was used as the base language for the templates created for the site.

#### Packages Used

* VS Code was used to develop the site
* Git was utilised for version control and transferring files between the code editor and the repository
* GitHub was utilised for storing the files for this project
* Balsamiq was utilised to develop wireframes for the site from which the design was based
* Adobe Illustrator was used to adapt images for use within the site.
* DrawSQL.app was used to develop the database schema during development

#### Resources Used

* The Django documentation was used extensively during development of this project
* The HTMX documentation was used as a reference source for the development of the HTMX features
* The Django AllAuth documentation was used as a reference and a guide for implementing the package and its features.
* The Cloudinary documentation was used extensively during development to setup the configuration between django and the cloudinary apis
* The Code Institute reference material was used as a general reference for things that I had previously done during the course.
* All other resources used are referenced where appropriate.


##### Other Libraries Used

## Deployment

The site was deployed via Heroku, and the live link can be found here - [The Pantry](https://pp4-the-pantry.herokuapp.com/)

### Project Deployment

To deploy the project through Heroku I followed these steps:
* Sign up / Log in to [Heroku](https://www.heroku.com/)
* From the main Heroku Dashboard page select 'New' and then 'Create New App'
* Give the project a name - I entered The-Pantry and select a suitable region, then select create app. The name for the app must be unique.
* This will create the app within Heroku and bring you to the deploy tab. From the submenu at the top, navigate to the resources tab.
* Add the database to the app, in the add-ons section search for 'Heroku Postgres', select the package that appears and add 'Heroku Postgres' as the database
* Navigate to the setting tab, within the config vars section copy the DATABASE_URL to the clipboard for use in the Django configuration.
* Within the django app repository create a new file called env.py - within this file import the os library and set the environment variable for the DATABASE_URL pasting in the address copied from Heroku. The line should appear as os.environ["DATABASE_URL"]= "Paste the link in here"
* Add a secret key to the app using os.environ["SECRET_KEY"] = "your secret key goes here"
* Add the secret key just created to the Heroku Config Vars as SECRET_KEY for the KEY value and the secret key value you created as the VALUE
* In the settings.py file within the django app, import Path from pathlib, import os and import dj_database_url
* insert the line if os.path.isfile("env.py"): import env
* remove the insecure secret key that django has in the settings file by default and replace it with SECRET_KEY = os.environ.get('SECRET_KEY')
* replace the databases section with DATABASES = { 'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))} ensure the correct indentation for python is used.
* In the terminal migrate the models over to the new database connection
* Navigate in a browser to cloudinary, log in, or create an account and log in. 
* From the dashboard - copy the CLOUDINARY_URL to the clipboard
* in the env.py file created earlier - add os.environ["CLOUDINARY_URL"] = "paste in the Url copied to the clipboard here"
* In Heroku, add the CLOUDINARY_URL and value copied to the clipboard to the config vars
* Also add the KEY - DISABLE_COLLECTSTATIC with the Value - 1 to the config vars
* this key value pair must be removed prior to final deployment
* Add the cloudinary libraries to the list of installed apps, the order they are inserted is important, 'cloudinary_storage' goes above 'django.contrib.staitcfiles' and 'cloudinary' goes below it.
* in the Settings.py file - add the STATIC files settings - the url, storage path, directory path, root path, media url and default file storage path.
* Link the file to the templates directory in Heroku TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
* Change the templates directory to TEMPLATES_DIR - 'DIRS': [TEMPLATES_DIR]
* Add Heroku to the ALLOWED_HOSTS list the format will be the app name given in Heroku when creating the app followed by .herokuapp.com
* In your code editor, create three new top level folders, media, static, templates
* Create a new file on the top level directory - Procfile
* Within the Procfile add the code - web: guincorn PROJECT_NAME.wsgi
* In the terminal, add the changed files, commit and push to GitHub
* In Heroku, navigate to the deployment tab and deploy the branch manually - watch the build logs for any errors.
* Heroku will now build the app for you. Once it has completed the build process you will see a 'Your App Was Successfully Deployed' message and a link to the app to visit the live site.

#### Forking the repository
By forking the GitHub Repository you can make a copy of the original repository to view or change without it effecting the original repository
This can be done by
    * Log into GitHub or create an account.
    * Locate the repository at https://github.com/MattBCoding/pp4-the-pantry .
    * At the top of the repository, on the right side of the page, select "Fork" from the buttons available.
    * A copy of the repository should now be created in your own repository.

#### Create a clone of this repository
Creating a clone enables you to make a copy of the repository at that point in time - this lets you run a copy of the project locally:
This can be done by:
* Navigate to https://github.com/MattBCoding/pp4-the-pantry
* click on the arrow on the green code button at the top of the list of files
* select the clone by https option and copy the URL it provides to the clipboard
* navigate to your code editor of choice and within the terminal change the directory to the location you want to clone the repository to.
* type 'git clone' and paste the https link you copied from github
* press enter and git will clone the repository to your local machine

### Acknowledgements

I'd like to thank the following:
* Daisy McGirr for all her help during this project.
* Sean and Ed at CI Tutor support for their patience and pointing me in the right direction when I went off course.