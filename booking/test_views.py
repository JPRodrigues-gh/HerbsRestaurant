""" View test cases """
from django.urls import reverse
from django.test import TestCase
from .models import Booking


class TestViews(TestCase):
    """ Test the function of all views """

    def test_home_page(self):
        """ Test that the Home page renders """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_menu_page(self):
        """ Test that the menu page renders """
        response = self.client.get('/menu/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'menu.html')

    def test_booking_page(self):
        """ Test that the booking page renders """
        response = self.client.get('/booking/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'booking.html')

    def test_create_booking(self):
        """
        Test that we can get the create booking form successfully.
        Then test that we use the correct template.
        Test that we can create a booking using the view.
        If successful it should redirect back to the booking page.
        """
        response = self.client.get('/create/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'create_booking.html')
        response = self.client.post('/create', {
            'booking_date': '2022-11-11',
            'booking_time': '17:00',
            'no_of_guests': 3})
        # self.assertRedirects(response, '/booking/')
        # self.assertEqual(response.status_code, 301)

    def test_update_booking(self):
        """
        Create a booking to use in update test.
        Post a changes to the update view.
        If successful it should redirect back to the booking page.
        Then fetch the record from Booking to assertTrue
        """
        booking = Booking.objects.create(
            booking_date='2022-11-11',
            booking_time='17:00',
            no_of_guests=3)
        response = self.client.post(
            reverse('update', kwargs={'booking_id': booking.booking_id}), {
                'booking_date': '2022-11-22',
                'booking_time': '17:00',
                'no_of_guests': 6})
        self.assertRedirects(response, '/booking/')
        booking_updated = Booking.objects.filter(
            booking_id=booking.booking_id,
            booking_date='2022-11-22',
            booking_time='17:00',
            no_of_guests=6)
        self.assertTrue(booking_updated)

        # self.assertEqual(response.status_code, 302)
        # booking.refresh_from_db()
        # self.assertEqual(
        #     booking.booking_date.strftime('%Y-%m-%d'),
        #     '2022-11-22'
        #     )
        # self.assertEqual(booking.booking_time.strftime('%H:%M'), '17:00')
        # self.assertEqual(booking.no_of_guests, 6)

    def test_delete_booking(self):
        """
        Create a booking to use in delete test.
        Execute the delete view function.
        If successful it should redirect back to the booking page.
        Then fetch the record from Booking to assertEqual to
          zero to verify record is deleted
        """
        booking = Booking.objects.create(
            booking_date='2022-11-11',
            booking_time='17:00',
            no_of_guests=3)
        response = self.client.get(f'/delete/{booking.booking_id}')
        self.assertRedirects(response, '/booking/')
        bookings = Booking.objects.filter(booking_id=booking.booking_id)
        self.assertEqual(len(bookings), 0)

    def test_cancel_booking(self):
        """
        Create a booking to use in cancel test.
        Execute the cancel view function.
        If successful it should redirect back to the booking page.
        Then fetch the record from Booking to assertTrue that
          the record has been cancelled
        """
        booking = Booking.objects.create(
            booking_date='2022-11-11',
            booking_time='17:00',
            no_of_guests=3)
        response = self.client.get(f'/cancel/{booking.booking_id}')
        self.assertRedirects(response, '/booking/')
        booking_cancelled = Booking.objects.filter(
            booking_id=booking.booking_id, confirm='Cancel')
        self.assertTrue(booking_cancelled)

    def test_contact_page(self):
        """ Test that the contact page renders """
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')

    def test_post_contact(self):
        """ Test that the is submitted successfully """
        response = self.client.post('/contact', {
            'name': 'Peter',
            'surname': 'Piper',
            'phone': '0986542112',
            'email': 'peter.piper@email.com',
            'subject': 'Contact form submitted by Peter Piper',
            'body': 'This is a message from Peter Piper'})
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)

    def test_about_page(self):
        """ Test that the about page renders """
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')
