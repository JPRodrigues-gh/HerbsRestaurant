""" ContactForm test cases """
from django.test import TestCase
from .forms import ContactForm


class TestContactForm(TestCase):
    """ Test validity of ContactForm fields """

    def test_name_field_is_required(self):
        """
        Test that the name field is required by leaving it blank
          but completing other required fields
        The test will verify that the error message is displayed.
        The test asserts whether or not there's a name key in the
          dictionary of form errors.
        Test that the name field is required.
        """
        form = ContactForm(
            {'name': '',
             'surname': 'Piper',
             'phone': '0875432211',
             'email': 'peter.piper@email.com',
             'subject': 'Contact form submitted by Peter Piper',
             'body': 'This is a message from Peter Piper'})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_surname_field_is_required(self):
        """
        Test that the surname field is required by leaving it blank
          but completing other required fields
        The test will verify that the error message is displayed.
        The test asserts whether or not there's a name key in the
          dictionary of form errors.
        Test that the surname field is required.
        """
        form = ContactForm(
            {'name': 'Peter',
             'surname': '',
             'phone': '0875432211',
             'email': 'peter.piper@email.com',
             'subject': 'Contact form submitted by Peter Piper',
             'body': 'This is a message from Peter Piper'})
        self.assertFalse(form.is_valid())
        self.assertIn('surname', form.errors.keys())
        self.assertEqual(form.errors['surname'][0], 'This field is required.')

    def test_phone_field_is_not_required(self):
        """
        Test that the phone field is not required
          by only completing required fields
        """
        form = ContactForm(
            {'name': 'Peter',
             'surname': 'Piper',
             'phone': '',
             'email': 'peter.piper@email.com',
             'subject': 'Contact form submitted by Peter Piper',
             'body': 'This is a message from Peter Piper'})
        self.assertTrue(form.is_valid())

    def test_email_field_is_required(self):
        """
        Test that the email field is required by leaving it blank
          but completing other required fields
        The test will verify that the error message is displayed.
        The test asserts whether or not there's a name key in the
          dictionary of form errors.
        Test that the email field is required.
        """
        form = ContactForm(
            {'name': 'Peter',
             'surname': 'Piper',
             'phone': '0875432211',
             'email': '',
             'subject': 'Contact form submitted by Peter Piper',
             'body': 'This is a message from Peter Piper'})
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors.keys())
        self.assertEqual(form.errors['email'][0], 'This field is required.')

    def test_subject_field_is_required(self):
        """
        Test that the subject field is required by leaving it blank
          but completing other required fields
        The test will verify that the error message is displayed.
        The test asserts whether or not there's a name key in the
          dictionary of form errors.
        Test that the subject field is required.
        """
        form = ContactForm(
            {'name': 'Peter',
             'surname': 'Piper',
             'phone': '0875432211',
             'email': 'peter.piper@email.com',
             'subject': '',
             'body': 'This is a message from Peter Piper'})
        self.assertFalse(form.is_valid())
        self.assertIn('subject', form.errors.keys())
        self.assertEqual(form.errors['subject'][0], 'This field is required.')

    def test_body_field_is_required(self):
        """
        Test that the body field is required by leaving it blank
          but completing other required fields
        The test will verify that the error message is displayed.
        The test asserts whether or not there's a name key in the
          dictionary of form errors.
        Test that the body field is required.
        """
        form = ContactForm(
            {'name': 'Peter',
             'surname': 'Piper',
             'phone': '0875432211',
             'email': 'peter.piper@email.com',
             'subject': 'Contact form submitted by Peter Piper',
             'body': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('body', form.errors.keys())
        self.assertEqual(form.errors['body'][0], 'This field is required.')

    def test_only_required_fields_are_in_form_metaclass(self):
        """
        Test to ensure that the only necessary fields are displayed in the form
          ie. no fields were added that should not be visible to the user.
        Instantiate an empty form and then assertEqual to check whether the
          form.meta.fields attribute is equal to a list of fields
        """
        form = ContactForm()
        self.assertEqual(
            form.Meta.fields, [
                'name',
                'surname',
                'phone',
                'email',
                'subject',
                'body'
                ]
            )
