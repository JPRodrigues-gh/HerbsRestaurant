"""
create forms directly from the model itself and
allow Django to handle all the form validation
"""
from django.forms import ModelForm
from .models import Contact, Booking


class ContactForm(ModelForm):
    """
    ContactForm inherits all the functionality of forms.ModelForm
    """
    class Meta:
        """
        Provide inner class Meta to tell the form
         which model it's going to be associated with.
        This inner class just gives our form some information
         about itself, like which fields it should render,
         how it should display error messages and so on
        """
        model = Contact
        fields = [
            'name',
            'surname',
            'phone',
            'email',
            'subject',
            'body']


class BookingForm(ModelForm):
    """
    BookingForm inherits all the functionality of forms.ModelForm
    """
    class Meta:
        """
        Provide inner class Meta to tell the form
         which model it's going to be associated with.
        This inner class just gives our form some information
         about itself, like which fields it should render,
         how it should display error messages and so on
        """
        model = Booking
        fields = [
            'booking_date',
            'booking_time',
            'no_of_guests',
            'confirm']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['confirm'].disabled = True
