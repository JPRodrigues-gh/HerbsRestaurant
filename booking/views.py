from django.shortcuts import render, redirect
from django.conf import settings
from django.core.mail import send_mail, send_mass_mail, BadHeaderError
from django.views import generic
from .models import Booking, Contact
from .forms import ContactForm
import os

default_email = os.environ.get('DEFAULT_FROM_EMAIL')

def index(request):
    return render(request, 'index.html')


def menu(request):
    return render(request, 'menu.html')


# The Contact Form section

# Render form as part of the view
def add_contact(request):
    """Provide a means for users to add items"""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            try:
                name = request.POST['name']
                subject = request.POST['subject']
                email = request.POST['email']
                body = request.POST['body']
                email_from = settings.EMAIL_HOST_USER
                # datatuple = (
                #     (subject, body, email_from, [email]),
                #     (subject, body, email_from, [email_from,]),
                # )
                # send_mass_mail(datatuple, fail_silently=False)
                send_mail(subject, body, email_from, [email])
                send_mail(subject, body, email_from, [email_from])

            except BadHeaderError:
                return HttpResponse('Invalid header found.')
    form = ContactForm()
    context = {
        'form': form
    }
    return render(request, 'contact.html', context)


def about(request):
    return render(request, 'about.html')


def view_booking(request):
    """ View of Booking table """
    bookings = Booking.objects.order_by('booking_date').all()
    context = {
        'bookings': bookings
    }
    template_name = 'booking.html'
    return render(request, template_name, context)
    # paginate_by = 10
