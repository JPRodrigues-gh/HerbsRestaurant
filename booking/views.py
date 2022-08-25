""" Views py for all booking app views """
import os
import datetime

from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError
from .models import Booking
from .forms import ContactForm, BookingForm


default_email = os.environ.get('DEFAULT_FROM_EMAIL')


def index(request):
    """ Render the home page """
    return render(request, 'index.html')


def menu(request):
    """ Render the menu page """
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
    """ Render the about page """
    return render(request, 'about.html')


# The Booking Form section
def view_booking(request):
    """ View of Booking table """
    if request.user.is_authenticated:
        bookings = Booking.objects.filter(booking_date__gte=datetime.date.today(), login_email=request.user.email).order_by('booking_date').all()
        context = {
            'bookings': bookings
        }
        template_name = 'booking.html'
        return render(request, 'booking.html', context)
    return render(request, 'booking.html')


def create_booking(request):
    """Provide a means for users to add bookings"""
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.login_email = request.user.email
            form.save()
            try:
                booking_date = request.POST['booking_date']
                booking_time = request.POST['booking_time']
                no_of_guests = request.POST['no_of_guests']
                login_email = request.user.email
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('booking')
    form = BookingForm()
    context = {
        'form': form
    }
    return render(request, 'create_booking.html', context)


def update_booking(request, booking_id):
    """Provide a means for users to change bookings"""
    booking_id = get_object_or_404(Booking, booking_id=booking_id)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking_id)
        if form.is_valid():
            if form.confirm == 1:
               form = form.save(commit=False)
               form.confirm = 0
            form.save()
            return redirect('booking')
    form = BookingForm(instance=booking_id)
    context = {
        'form': form
    }
    return render(request, 'update_booking.html', context)


def delete_booking(request, booking_id):
    """Provide a means for users to cancel bookings"""
    booking_id = get_object_or_404(Booking, booking_id=booking_id)
    booking_id.delete()
    return redirect('booking')
