""" ContactForm test cases """
from django.test import TestCase
from .forms import BookingForm


class TestContactForm(TestCase):
    """ Test validity of ContactForm fields """

    def test_booking_date_field_is_required(self):
        """
        Test that the booking_date field is required by leaving it blank
          but completing other required fields
        The test will verify that the error message is displayed.
        The test asserts whether or not there's a name key in the
          dictionary of form errors.
        Test that the booking_date field is required.
        """
        form = BookingForm(
            {'booking_date': '',
             'booking_time': '17:00',
             'table_id': 'A1',
             'no_of_guests': '3'})
        self.assertFalse(form.is_valid())
        self.assertIn('booking_date', form.errors.keys())
        self.assertEqual(
            form.errors['booking_date'][0], 'This field is required.')

    def test_booking_time_field_is_required(self):
        """
        Test that the booking_time field is required by leaving it blank
          but completing other required fields
        The test will verify that the error message is displayed.
        The test asserts whether or not there's a name key in the
          dictionary of form errors.
        Test that the booking_time field is required.
        """
        form = BookingForm(
            {'booking_date': '2022-09-14',
             'booking_time': '',
             'table_id': 'A1',
             'no_of_guests': '3'})
        self.assertFalse(form.is_valid())
        self.assertIn('booking_time', form.errors.keys())
        self.assertEqual(
            form.errors['booking_time'][0], 'This field is required.')

    def test_table_id_field_is_required(self):
        """
        Test that the table_id field is required by leaving it blank
          but completing other required fields
        The test will verify that the error message is displayed.
        The test asserts whether or not there's a name key in the
          dictionary of form errors.
        Test that the table_id field is required.
        """
        form = BookingForm(
            {'booking_date': '2022-09-14',
             'booking_time': '17:00',
             'table_id': '',
             'no_of_guests': '3'})
        self.assertFalse(form.is_valid())
        self.assertIn('table_id', form.errors.keys())
        self.assertEqual(
            form.errors['table_id'][0], 'This field is required.')

    def test_no_of_guests_field_is_required(self):
        """
        Test that the no_of_guests field is required by leaving it blank
          but completing other required fields
        The test will verify that the error message is displayed.
        The test asserts whether or not there's a name key in the
          dictionary of form errors.
        Test that the no_of_guests field is required.
        """
        form = BookingForm(
            {'booking_date': '2022-09-14',
             'booking_time': '17:00',
             'table_id': 'A1',
             'no_of_guests': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('no_of_guests', form.errors.keys())
        self.assertEqual(
            form.errors['no_of_guests'][0], 'This field is required.')

    def test_only_required_fields_are_in_form_metaclass(self):
        """
        Test to ensure that the only necessary fields are displayed in the form
          ie. no fields were added that should not be visible to the user.
        Instantiate an empty form and then assertEqual to check whether the
          form.meta.fields attribute is equal to a list of fields
        """
        form = BookingForm()
        self.assertEqual(
            form.Meta.fields, [
                'booking_date',
                'booking_time',
                'no_of_guests',
                'table_id',
                'confirm'
                ]
            )
