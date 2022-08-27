""" View test cases """
from django.urls import reverse
from django.test import TestCase
from .models import Booking


class TestViews(TestCase):
    """ Test the function of all views """

    def test_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_menu_page(self):
        response = self.client.get('/menu/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'menu.html')

    def test_booking_page(self):
        response = self.client.get('/booking/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'booking.html')

    def test_create_booking(self):
        response = self.client.get('/create/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'create_booking.html')
        response = self.client.post('/create', {
            'booking_date': '2022-11-11',
            'booking_time': '17:00',
            'no_of_guests': 3})

    def test_update_booking(self):
        booking = Booking.objects.create(
            booking_date='2022-11-11',
            booking_time='17:00',
            no_of_guests=3)
        response = self.client.post(
            reverse('update', kwargs={'booking_id': booking.booking_id}), {
                'booking_date': '2022-11-22',
                'booking_time': '17:00',
                'no_of_guests': 6})
        self.assertEqual(response.status_code, 302)
        booking.refresh_from_db()
        self.assertEqual(
            booking.booking_date.strftime('%Y-%m-%d'),
            '2022-11-22'
            )
        self.assertEqual(booking.booking_time.strftime('%H:%M'), '17:00')
        self.assertEqual(booking.no_of_guests, 6)
        # self.assertRedirects(response, booking)
    #     self.assertFalse(updated_booking.status_code, 200)
    #     self.assertTemplateUsed(response, 'update_booking.html')

    # def test_delete_booking(self):
    #     response = self.client.get('/delete/')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'booking.html')

    # def test_cancel_booking(self):
    #     response = self.client.get('/cancel/')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'booking.html')

    def test_contact_page(self):
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')

    def test_post_contact(self):
        response = self.client.post('/contact', {
            'name': 'Peter',
            'surname': 'Piper',
            'phone': '0986542112',
            'email': 'peter.piper@email.com',
            'subject': 'Contact form submitted by Peter Piper',
            'body': 'This is a message from Peter Piper'})
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')

    def test_about_page(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')
