![pic](/readme/mockup/mockup_pick_me_up.jpg)
# [Pick Me Up](https://pick-me-up-project.herokuapp.com/) (Milestone project 4)

## Table of Contents

1. [Introduction](#introduction)<br/>
2. [UX](#ux)<br/>
3. [Features](#features)<br/>
4. [Database architecture](#database-architecture)<br/>
5. [Technologies Used](#technologies-used)<br/>
6. [Testing](#testing)<br/>
7. [Critical Bug in the production setup](#critical-bug-in-the-production-setup)
8. [Deployment](#deployment)<br/>
9. [Content](#content)<br/>
10. [Media](#media)<br/>
11. [Acknowledgements](#acknowledgements)<br/>
12. [Disclaimer](#disclaimer)<br/>

<br>

## Introduction

[Pick-me-up](https://pick-me-up-project.herokuapp.com/) is a python based application website, developed with the Django framework.
This website aims to sell coffee and cocoa beans. Yes, these are from two different plants, but they have very similar aims; to stimulate and energize. 
The name of the website can brilliantly imply these. 
In the first look, Pick-me-up can be indicated as a webshop to pick up and buying something. But, it also can imply be stimulating and energizing (if you stress it on me! word).

The coffee and chocolate industry evolved rapidly over the years. 
The mass production of the beans caused lower quality. 
This website aims to sell the better quality of these two amazing fruits.

## UX

This website will present shoppers with coffee and cocoa beans in a user-friendly interface. 
Shopper, can view the list of the beans, search and sort the products. 
Also, it would be possible to see more details about individual products, 
for example, what is the origin of the beans and in which form they can be purchased. 
This website consists of four main sections. First, viewing and navigation, in this part user 
can see a list of different products, look at the individual product details. Also, users can 
find out about different deals and special offers. Second, registration and user account, 
in this section user can create a personalized user profile, log in and logout, recover 
their password in case of forgotten, and receive a confirmation email after registration. 
Third, searching and sorting, in this section user can sort available products by name or 
different properties like price or rating. Also, can search through the name and description of available products. 
Forth, purchasing and checkout, 
easily select the type and quantity of the product and doing the safe purchasing procedure. 
Also, in the user profile, users can look at their order history.

Here some user stories:

* As a coffee lover , this website to find unique coffees which are not available in normal stores.
* As a shopper, I like special offers.
* As a user, this webpage help me to understand about different type of coffee and cocoa beans.

The desktop and mobile resolution wireframes of the Book Review Club can be found in the following links:

* [Home page desktop](/readme/wireframes/wireframe-home-page-desktop.png) 
* [Home page mobile](/readme/wireframes/wireframe-home-page-mobile.png)
* [Main page desktop](/readme/wireframes/wireframe-main-page-desktop.png)
* [Main page mobile](/readme/wireframes/wireframe-main-page-mobile.png) 

## Features

In the following table, implemented features, and possible future features are presented:

| Implemented Features | Possible Future Features|
| :------------- | :---------- |
|Navigation menu: <br> - Account, logo, shopping basket, structured layouts, search bar | Add review feature: <br> - User add review and products get interactive rating based on the users average rating
| Home page: <br> - Intro to the website | Add Customer purchase follow-up: <br> - Customers can re-order previously purchase products without the need to the shopping process again and again
| Products overview page: <br> - Product overviews including product type, category, rating. Also, it is possible to sort the coffee and cocoa beans based on the price, rating, name and category <br> - Possibly to edit and delete for the admin user | Register feature: <br> - User can register/login with their Gmail, Facebook or other accounts
| Product detail page: <br> - Product details page including, product description, flavor that is in addition to products overview information in the above <br> - Possibility to add limited and specific amount of the product to the basket|
| Basket page: <br> - Look at the overview of the added products in the basket, and possibility to modify or delete them  from the basket|
| Checkout page: <br> - Getting the customer delivery info for checkout procedure <br> - User can check out without being registered <br> - Payment use Stripe and webhook handler <br> - Email conformation and shopping summary is available after purchasing |
| Profile page: <br> - User can register to have his/her default delivery information saved <br> - Purchase history/summary is available for registered user <br> - Admin user have possibility to add, edit, delete products in this section |

## Database architecture

In the development step of the project, sqlite3 is used for handling the database. 
During the production step of the project, the database was switched to 
PostgreSQL with Heroku as an add-on. Databases have been set up in ``models.py`` of the apps; 
checkout app with subclasses Receipt, ReceiptLineItem, products app with subclasses Category, 
Product and UserProfile app with subclasses UserProfile.
The database structure can be seen in the following image:

![pic](/readme/database/database-structure.PNG)

## Technologies Used

The following technologies have been used in this project:


* [HTML5](https://www.w3.org/TR/html52/), is used as markup language for documents design of the web browser.
* [CSS](https://www.w3.org/Style/CSS/Overview.en.html/), is used as style sheet language used for styling HTML.
* [JavaScript](https://www.javascript.com/), is used for interactive UX in adding product feature, update amount products in the basket, Stripe payment, …
* [Jquery](https://jquery.com/), mostly JavaScript is used in the form of JQuery to simplify DOM manipulation.
* [Bootstrap](https://getbootstrap.com/), is used for customizing front-end of the website.
* [Python 3.8.2](https://www.python.org/downloads/release/python-382/), is used as logic programing language.
* [Jinja](https://jinja.palletsprojects.com/en/2.11.x/), is used as templating language.
* [Django Framework](https://www.djangoproject.com/), mostly Python is used in the form of the Django as the main framework of this project.
* [Django Allauth](https://django-allauth.readthedocs.io/en/latest/installation.html), is used for user registration features.
* [Django Crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/), is used for controlling form functionality.
* [SQLite](https://www.sqlite.org/download.html), is used as database in development mode for Django.
* [PostgreSQL](https://www.postgresql.org/), is used as database in production mode.
* [Psycopg2](https://pypi.org/project/psycopg2/), is used as adapter between PostgreSQL and Django.
* [Stripe](https://stripe.com/en-se/), is used in for the payment functionality.
* [Heroku](https://www.heroku.com/), is used as a cloud platform for deploying the project.
* [Gunicorn](https://gunicorn.org/), is used for deploying Django to Heroku.
* [AWS](https://aws.amazon.com/), is used to store media and static files in production.
* [Google Font](https://fonts.google.com/), is used for formatting the fonts.
* [Fontawsome](https://fontawesome.com/), is used to create icons.
* [Adobe Photoshop](https://www.adobe.com/): is used to edit images.
* [Balsamic](https://balsamiq.com/), is used to demonstrate the main wireframe and design idea of the poject.

## Testing

### Django Python testing:

It has been tried to test the views with the Django testing feature, here are the results for the following apps: **home, products, basket, profiles**

### home

```
Name                          Stmts   Miss  Cover
-------------------------------------------------
home/__init__.py                  0      0   100%
home/admin.py                     1      0   100%
home/apps.py                      3      3     0%
home/migrations/__init__.py       0      0   100%
home/models.py                    1      0   100%
home/test_views.py                6      0   100%
home/tests.py                     1      0   100%
home/urls.py                      3      0   100%
home/views.py                     3      0   100%
-------------------------------------------------
TOTAL                            18      3    83%
```

### products 

```
Name                                  Stmts   Miss  Cover
---------------------------------------------------------
products/__init__.py                      0      0   100%
products/admin.py                         9      0   100%
products/apps.py                          3      3     0%
products/forms.py                         9      0   100%
products/migrations/0001_initial.py       6      0   100%
products/migrations/__init__.py           0      0   100%
products/models.py                       22      3    86%
products/test_views.py                   47      0   100%
products/tests.py                         0      0   100%
products/urls.py                          3      0   100%
products/views.py                        92     34    63%
---------------------------------------------------------
TOTAL                                   191     40    79%
```

### basket 

```
Name                                  Stmts   Miss  Cover
---------------------------------------------------------
basket/__init__.py                        0      0   100%
basket/admin.py                           0      0   100%
basket/apps.py                            3      3     0%
basket/contexts.py                       17      4    76%
basket/migrations/__init__.py             0      0   100%
basket/models.py                          0      0   100%
basket/templatetags/__init__.py           0      0   100%
basket/templatetags/basket_tools.py       5      1    80%
basket/test_views.py                      6      0   100%
basket/tests.py                           0      0   100%
basket/urls.py                            3      0   100%
basket/views.py                          40     31    22%
---------------------------------------------------------
TOTAL                                    74     39    47%
```

### profiles
```
Name                                  Stmts   Miss  Cover
---------------------------------------------------------
profiles/__init__.py                      0      0   100%
profiles/admin.py                         1      0   100%
profiles/apps.py                          3      3     0%
profiles/forms.py                        18      1    94%
profiles/migrations/0001_initial.py       8      0   100%
profiles/migrations/__init__.py           0      0   100%
profiles/models.py                       19      1    95%
profiles/test_views.py                    9      0   100%
profiles/tests.py                         1      0   100%
profiles/urls.py                          3      0   100%
profiles/views.py                        26     10    62%
---------------------------------------------------------
TOTAL                                    88     15    83%
```

### Manual testing:

It has been tried to define different possible scenarios to see if the web apps function as expected.

### Non-registered user try to do a complete shopping procedure:

1. User can realize can **SHOP COFFEE AND CACAO BEANS HERE**, and by clicking on 
the **WELCOME** button can proceed to the shop and look at all products. Users 
can look at specific products like **COFFEE, COCOA, or SPECIAL OFFERS**. Also, users 
can search for the name or description of the products. The test results can be found in the following [link](/readme/test/test-01.jpg).

2. The User clicks on the **WELCOME** button to look at all the available products in the web store. 
In this section, the user can sort the products with their Name, Price, Rating, and the categories they belong to. 
The user decides to sort the product with the sort feature. the user would like to sort coffees based on their rating 
from highest to lowest. All the links are tested, and they function accordingly. 
The test results can be found in the following link. [link](/readme/test/test-02.jpg).

3. The User decides to read more about the products with the highest rating by clicking on the image.
 The user can go back to the products page **(PRODUCTS)** or add **(ADD)** the product to the basket. 
 The user decides to choose 3 kg of the coffee beans in the basket, by click on the **ADD** button. 
 A message confirms the product added to the basket and the price and the color of the cart change 
 indicating the coffee beans in the basket. All the links are tested, and they function accordingly. 
 The test results can be found in the following [link](/readme/test/test-03.jpg).

4. The user decides to proceed to the basket and view the products in the basket, 
this can be done by clicking on the updated cart in the top right corner of the browser. 
In this section, the user can look at the summary of the products, including name, image, price per kg 
and quantity of the shopping, and the price calculated. The user can proceed to checkout **(CHECKOUT)** 
or go back to the products page **(PRODUCTS)**. The user can see there is a 15% tax included in the total payment price. 
The user decides to modify the amount of the coffee beans to two kg instead. 
This is possible from this section by changing and updating **(UPDATE)** the amount. 
All the prices for the subtotal and total will modify accordingly. All the links are tested, and they function accordingly. 
The test results can be found in the following [link](/readme/test/test-04.jpg).

5. The user decides to proceed to checkout, by click on the **(CHECKOUT)** buttons. 
User-provided to fill in the required information for checkout procedure. 
User can see if he/she was registered or have an account, could save this information to his/her profile. 
But, this doesn’t affect the check-out procedure and the user still can do the checkout procedure. 
User, fill in the information. If the user does not fill in the required information or there is a problem with the 
card payment method controlled with Stripe, an appropriate warning/error message displayed to the user. Also, the user 
can go back to the basket section **(BASKET)**. User, fill in the correct form and Stripe test card number **(4242 4242 4242 4242)** 
and proceed to the purchase **(PURCHASE)**. All the links are tested, and they function accordingly. 
The test results can be found in the following [link](/readme/test/test-05.jpg).

6. The user was directed to a page that shows the receipt number and summary of the purchase. 
The user can go back to the products. It is also mentioned that a confirmation message will be sent
 to his/her email. All the links are tested, and they function accordingly.
  The test results can be found in the following [link](/readme/test/test-06.jpg).


### A registered user try to do a complete shopping procedure:

In this scenario user first try to make a user profile account before purchasing.

7. The user could use the account section in the top left of the browser to log in 
and create his/her profile. Use choose to signup to the page. The user 
was redirected to the signup section the fill in the required information. 
A confirmation link sends to the user email for the confirmation procedure. By clicking on the 
link user was redirected to confirm the email **(CONFIRM)**. It is important to mention that in the 
development mode the link will be sent to the user CLI and the user need to manually add the 
link after /accounts to the base URL to be redirected to the 
confirmation email page. The test results can be found in the following [link](/readme/test/test-07.jpg).

8. The user can see that successfully logged in to the site, with seeing the 
username in the account section and the color of the account icon changed. 
Logged in user can set the profile information 
and logout from the page. The test results can be found in the following [link](/readme/test/test-08.jpg).

9. The shopping procedure is the same as an unregistered user and will not be repeated here. 
But user decides to use the search bar to search for some products with the ‘delicious’ keyword. 
the user chooses all these three products and removes one of the coffee from the shopping cart. 
The shopping procedures were tested for the unregistered user and will not be repeated here. 
The test results can be found in the following [link](/readme/test/test-09.jpg).

10. On the checkout page, the user can see that can save the required information 
for delivery to the profile. And the confirmation email sends to the user mailbox. 
The test results can be found in the following [link](/readme/test/test-10.jpg).

11. Going back to the user profile, the user could see the saved delivery information to the 
left of the page and receipts history to the right of the 
page and by clicking on the receipt number user can get more detail for the specific shopping. 
The test results can be found in the following [link](/readme/test/test-11.jpg).

### Admin user can add/edit/ delete products from the site:

In this section, it is tested that admin user (superuser) can add/edit/delete a product:

12. If the user account is defined as a superuser can add/edit/delete products. 
The add product form is controlled with the model requirement, for example, 
if the user adds a price with more than 6 digits will get the error message. 
The admin user can add a product without an image. 
Then the user will be redirected to the added product page. 
The test results can be found in the following [link](/readme/test/test-12.jpg).

13. the user can edit the added products. For example, 
the admin user decided to change the price from 99.99 to 11.11 for the product.
The test results can be found in the following [link](/readme/test/test-13.jpg).

14. the user can delete the product and the user will be redirected to all products page. 
The test results can be found in the following [link](/readme/test/test-14.jpg).

### A user get a customized HTTP response for the errors 400, 403,404, 500

15. The user tried to go to the endpoint which there is not URL defied for it, the proper 404 response showed on the page,
 which the user could be redirected to the home page. The test results can be found in the following [link](/readme/test/test-15.jpg).

## Website validation on different browser and mobile devices

The website was tested on the following browsers with the above scenarios 
and there was no problem regarding the functionality of the web apps. 

* Google chrome
* Firefox
* Opera
* Microsoft edge
* Samsung S8
* Iphone 8

## Different validation services

### Markup Validation Service W3C®

The HTML part is validated with Markup Validation Service W3C® without any major problem. 
There was some minor issue regarding using ul element for the list elements which was resolved. 
HTML was validated for the following endpoints without a problem and there is just a warning about 
“type attribute is not necessary for JavaScript resources”.

The test results can be found in the following [link](/readme/test/test-html.jpg).

### W3C® CSS validation service

The W3C® CSS validation service was used for the CSS part. There was no problem regarding CSS validating, 
but there some issue regarding bootstrap. Results can be seen in the following link.

The test results can be found in the following [link](/readme/test/test-css.jpg).

### JS hint

JS hint used for validation of JavaScript. There is no problem to report. 
There was a just few missing semicolons that were fixed. 
And, undefiled variable $ which can be ignored.

The test results can be found in the following [link](/readme/test/test-js.jpg).

## Critical bug in the production setup

This application website using a free Gmail SMTP server for the SignUp/SignIn procedure. 
In the Gmail email settings web app administrator need to activate a two-step verifications 
method, this will provide an app password specific to this Django app. Later, this Gmail 
address and the password could be used in the Heroku app settings that allows to authenticate and use the 
Gmail account to send emails which are used for SignUp/SignIn procedures.

This could work fine after the deployment of the 
project and in real production. But, there is a chance that after a 
while google recognizes this as a security vulnerability for the Gmail 
account and automatically turns the security setting off. The explanation 
given by Google can be found in the following [link](https://support.google.com/accounts/answer/6010255?hl=en) and image below.

![pic](/readme/test/google-security-issue-bug.PNG)

This would lead to this issue that any SignUp/SignIn procedure 
leads to server error with code 500. So, it is highly recommended to check 
this setting is not off after a while the app is deployed to 
Heroku, and checking should be done regularly to prevent this issue.

## Deployment

This part explains how to, clone this repository from GitHub, or work the 
project from a local copy and finally deploy it to Heroku, for this purpose you need to have Python (version 3.0) 
installed, Github, Stripe, Gmail, AWS, and Heroku accounts.

It is possible to deploy this project in GitHub as your development environment, 
with following these steps:

#### Cloning of the Repository

In your IDE CLI type:

```
git clone https://github.com/MajPaji/Pick-me-up.git
```

#### Installing the Requirements

Install all requirements modules with following CL:

```
pip3 install -r requirements.txt
```

#### Setting up the environmental variables

In the Gitpod setting add the following variables:

| Name | Value|
| :------------- | :---------- |
| DEVELOPMENT | True
|SECRET_KEY | 'YourSecretKey'
|STRIPE_PUBLIC_KEY | 'YourStripePublickey'
|STRIPE_SECRET_KEY | 'YourStripeSecretkey'

#### Database Migrations

In your IDE CLI type:

```
python3 manage.py makemigrations 
```

```
python3 manage.py migrate
```

#### Loading Fixtures

In your IDE CLI type with this following order type:

```
python3 manage.py loaddata categories.json 
```

```
python3 manage.py loaddata products.json
```
**Note:** make sure to first load categories file and the producs json file.

#### Create Superuser

To have administrative access to the website, one need to create superuser, in the IDE CLI type:

```
python3 manage.py createsuperuser
```
you need to choose username and password, email is optional, but it is recommended.

It is possible to run the project in localhost, in your IDE CLI type:

```
python3 manage.py runserver
```

Now, it is possible to run the website with ctrl+click on the ://127.0.0.1:8000/ link

### Deploying to Heroku

One needs to do the following steps to host this project to Heroku:

#### Setup the Heroku

* Create a Heroku account
* Create a new app and select your region

Prepare Local workspace for Heroku, Make a Procfile in the CLI:

```
echo web: gunicorn pick_me_up.wsgi:application > Procfile
```

(This is required for the Heroku to know at the entry point get the app up and running)

Install PostgreSQL as the database, with following command in CLI:

```
pip3 install psycopg2-binary
```
Install Gunicorn which works as the server for the app when is deployed to Heroku, in the CLI type:

```
pip3 install gunicorn
```
Update the requirements file, in the CLI type:

```
pip3 freeze --local > requirements.txt
```
#### Making the configuration variable in Heroku

In the Heroku app setting, in the Config Vars section, make the following Key and Value parameters

| Key | Value|
| :------------- | :---------- |
|AWS_ACCESS_KEY_ID| 'YourAWSKeyId'
|AWS_SECRET_ACCESS_KEY| 'YourSecretAccessKey'
|DATABASE_URL| 'YourDatabaseUrl'
|EMAIL_HOST_PASS| 'YourHsotPass'
|EMAIL_HOST_USER| 'Your Gmail address'
|SECRET_KEY| 'YourSecretKey'
|STRIPE_PUBLIC_KEY| 'YourStripePublickey'
|STRIPE_SECRET_KEY| 'YourStripeSecretkey'
|STRIPE_WH_SECRET| 'YourStripeWHSecretkey'
|USE_AWS| True

#### Adding the PostgreSQL database to Heroku

In the Heroku app Resources section, search for PostgreSQL and add it to your app, 
Back into the main project app setting comment out the defaults setting:

```
if 'DATABASE_URL' in os.environ:
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }

```

And just add:

```
DATABASES = {     
        'default': dj_database_url.parse("Your Postgres database URL")     
    }

```

**Importatnt:** Do not commit this changes, because it will expose 
Your Postgres database URL, this is just temporary to push the 
files to PostgreSQL and after should return to the default setting.

#### Migrate the database to PostgreSQL

In your IDE CLI type:

```
python3 manage.py makemigrations
```
```
python3 manage.py migrate
```

#### Loading Fixtures

In your IDE CLI type with this following order type:

```
python3 manage.py loaddata categories.json
```
```
python3 manage.py loaddata products.json
```

**Note:** make sure to first load categories file and the produces json file.

#### Create Superuser

To have administrative access to the webpage, one need to create superuser, in the IDE CLI type:

```
python3 manage.py createsuperuser
```

#### Push the files into the Heroku

In your IDE CLI type:

```
heroku login -i
```
fill in your username and password to connect to your Heroku, In your IDE CLI type:

```
git push heroku master
```

In the Heroku app, look into the Activity section, 
the live link will be available after deployment process to complete.

#### Gmail

In order to get EMAIL_HOST_PASS, look at the following setting for 
Google SMTP [documentation](https://support.google.com/a/answer/176600?hl=en#zippy=%2Cuse-the-gmail-smtp-server).

#### Storing Static and Media files in AWS

One can make the following setting to store static and media file be hosted in AWS, 
[AWS S3 bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html) and  [S3BotoStorage](https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html).

**Note:** media files needed to add manually the AWS S3 bucket

## Content

The product descriptions and images are mostly coming from:

* Coffee descriptions are coming from [eliteworldhotels.com.tr](https://www.eliteworldhotels.com.tr/blog-en/food-drink/for-coffee-lovers-7-different-types-of-coffee-beans-from-different-countries-and-their-characteristics.4.3373.aspx)

* COCOA descriptions are coming from [chocolatealchemy.myshopify.com](https://chocolatealchemy.myshopify.com/collections/cocoa-nibs)

## Media

The photos used in this site were obtained from website with right for free to use, share or modify, even commercially:

* The background image is from free image source [unsplash.com](https://unsplash.com/photos/XtUd5SiX464)

## Acknowledgements

I have started this course with this believe that I always wanted to be a software developer, 
or working in tech industry but because of many circumstances, I could not get into this area. 
Code Institute gave me the hope and knowledge which could help me to 
pursue my career in this area. So, I would like to give my sincere acknowledge to:

* Code institute management team to make this opportunity
* Gerard (Gerry) McBride, my mentor, 
for giving good key guidance through this project and the course and always on-time for the meetings even during weekends
* Code institute tutor team which try to help understands any 
issue and help you go through the problems. I specially would like to thank Scott, Igor and Tim.
* Slack community

## Disclaimer

Please contact if you have any issue regarding copyright content. This project is only for educational purposes. sababi@kth.se