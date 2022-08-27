# Herb's Restaurant Booking App

## Problem Statement
1. The user would like to book one or more guests for a meal in a restaurant at a particular time and date

## User Stories
1. Site Navigation: As a **Site User** I can **easily navigate the site** so that **I can view the menu, sign up, and manage my bookings**
2. Admin Manage bookings: As a **Site Admin** I can **create, view, update and cancel bookings** so that **I can manage my table bookings**
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
14. Admin Confirm bookings: As a **Site Admin** I can **approve bookings** so that **I can better plan bookings**
15. Password reset: As a **Site User** I can **request a password reset and receive email confirmation** so that **I can access my account if I have forgotten my password
16. Email Contact form: As a **Site User** I will **receive an email confirmation of my contact form submission**
17. Signup email verification: As a **Site User** I will **need to verify my signup via an email verification link**
18. About page: As a **Site User** I can **navigate to the About page** so that **I can view a brief intro to Herb’s Restaurant and it’s business hours
19. View Bookings: As a **Site User** I can **view all my booking** so that **I make better plan my events and also cancel or change bookings**
20. On Signup Add User: As a **Site User** when I **sign up** the app **will add my details to the user table**

## Testing

# Django Tests

* Created test cases to test the BookingForm. Test file name: test_bookingform.py
    * Tests to confirm that the form is only valid if all required fields are completed
    * Tests to confirm that only the necessary field are displayed on the form
* Created test cases to test the ContactForm. Test file name: test_contactform.py
    * Tests are run to confirm that the form is only valid if all required fields are completed
    * Tests to confirm that only the necessary field are displayed on the form
    * Not tested: Confirm field is read-only/disabled.
* Created test cases to test the all view templates render
* Created test case to test that adding a contact or submitting a contact form works as expected
* Created test cases to verify that the user can:
    * Create a booking
    * Update/make changes to a booking
    * Delete a booking
    * Mark a booking as cancelled
    * The option to cancel a booking is preferable, as the record will still be visible to the admin
    * Functionality can be added later to provide conditions permitting a user to delete a booking



## Bugs and Fixes

* Images not found when deployed to heroku
    * because some styles sheets and images definitions in the template were not in block tags
    * Also added {% load static %} to all templates due to block end error 
* Styling and images not found when deployed
    * installed whitenoise package
* Fixed variable EMAIL_USE_TLS, was incorrect as EMAIL_USES_TLS (Thanks Ian Meigh for spotting it for me - post in Slack)
    * After hours of figuring out how "it" works, then going through error after error, the brain swells and the simplest typo is blocked from your sight
* BookingAdmin class -- confirm functions -- admin.py
    * previously working (somehow) with two parameters, ```def confirm_booking(self, queryset):```, when simply changing confirm from 0 to 1 and vice versa. 0 being No and 1 being Yes.
    * after changing the field type from integer to char and adding an additional option of 'cancel' I received this error:
        * confirm_booking() takes 2 positional arguments but 3 were given
    * After scouring the web for possible causes I came up empty handed. I decided to look deeper into the detail and found my solution from looking into:
        * File "/workspace/.pip-modules/lib/python3.8/site-packages/django/contrib/admin/options.py", line 1408, in response_action response = func(self, request, queryset)
    * Adding 'request' as a second parameter solved the issue: ```def confirm_booking(self, request, queryset):```
* Booking template
    * after changing confirm field from integer to char in booking model I didn't remove the conditional statement from the booking template used to set confirm 0 to No and 1 to Yes. This displayed inconsistant values. 

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
- simpleisbetterthancomplex.com

## Deployment

* The link to the deployed app:

  * https://herbsrestaurant.herokuapp.com/

  * The app was deployed using the Heroku App
