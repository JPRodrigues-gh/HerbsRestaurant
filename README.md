# Herb's Restaurant Booking App

## Problem Statement
1. The user would like to book one or more guests for a meal in a restaurant at a particular time and date

## User Stories
1. Site Navigation: As a **Site User** I can **easily navigate the site** so that **I can view the menu, sign up, and manage my bookings**
2. Manage bookings: As a **Site Admin** I can **create, view, update and cancel bookings** so that **I can manage my table bookings**
3. Sign-up: As a **Site User** I can **register an account** so that **I can sign-in with username and password**
4. Reset password: As a **Site User** I can **reset my password myself** so that **I don't have to ask webmaster**
5. Sign-in with Social Networks: As a **Site User** I can **use a social network** so that **I can sign-in to the site**
6. View table availability: In order to **book a table** as a **Site User** I can **see available tables**
7. Make booking: As a **Site User** I can **make Date/time bookings**
8. Book multiple tables: As a **Site User** I can **make multiple table occupancy bookings** so that **I can take a larger party**
9. Change booking: As a **Site User** I can **update my booking** so that **I can increase or reduce the number of tables booked**
10. Change booking date: As a **Site User** I can **update my booking date** so that **I can change the date to earlier or later date**
11. Cancel booking: As a **Site User** I can **cancel a booking**
12. View menu: As a **Site User** I can **view the menu** so that **I can decide on meals beforehand**
13. Contact form: As a **Site User** I can **submit a contact form** so that **I can get support from the restaurant**
14. Confirm bookings: As a **Site Admin** I can **approve bookings** so that **I can better plan bookings**
15. Password reset: As a **Site User** I can **request a password reset and receive email confirmation** so that **I can access my account if I have forgotten my password

## Bugs and Fixes

* Images not found when deployed to heroku
    * because some styles sheets and images definitions in the template were not in block tags
    * Also added {% load static %} to all templates due to block end error 
* Styling and images not found when deployed
    * installed whitenoise package
* Fixed variable EMAIL_USE_TLS, was incorrect as EMAIL_USES_TLS (Thanks Ian Meigh for spotting it for me - post in Slack)
    * After hours of figuring out how "it" works, then going through error after error, the brain swells and the simplest typo is blocked from your sight

## Sources and References

### Website Design, Layout and function
- I used the "https://startbootstrap.com/previews/business-casual" as my template
- I used the part of social network links layout from my tourguide project
- The home page image I is from Pexel and icons_for_free
 - pexels-foodie-factor-551997.avif
 - pexels-rachel-claire-4577396.avif
- Used convertio.co, compressjpeg.com, cleancss.com, geeksforgeeks.org

### User account sign up and login functionality
- Guided by django blog project
- Support from stackoverflow.com, web.dev, slack
- django documentation

### General support
- djangoproject.com
- geeksforgeeks.org
- w3schools.com
- Slack
- stackoverflow

## Deployment

* The link to the deployed app:

  * https://herbsrestaurant.herokuapp.com/

  * The app was deployed using the Heroku App
