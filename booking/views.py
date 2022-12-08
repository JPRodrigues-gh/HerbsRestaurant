""" Views py for all booking app views """
import os
import datetime

from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages
from .models import Booking, Table
from .forms import ContactForm, BookingForm

default_email = os.environ.get('DEFAULT_FROM_EMAIL')
success_message = os.environ.get('SUCCESS_MESSAGE')


def index(request):
    """ Render the home page """
    return render(request, 'index.html')


def messenger(request, message):
    """ Render the messenger page """
    return render(request, 'messenger.html', message)


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
                send_mail(subject, body, email_from, [email])
                send_mail(subject, body, email_from, [email_from])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            messages.success(request, 'Your message has been submitted.')
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
        if request.user.username == 'admin':
            bookings = Booking.objects.filter(
                booking_date__gte=datetime.date.today()).order_by(
                    'booking_date', 'created_date').all()
        else:
            bookings = Booking.objects.filter(
                booking_date__gte=datetime.date.today(),
                login_email=request.user.email).exclude(
                    confirm='Cancel').order_by(
                        'booking_date').all()
        context = {
            'bookings': bookings
        }
        return render(request, 'booking.html', context)
    return render(request, 'booking.html')


def create_booking(request):
    """Provide a means for users to add bookings"""
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            # verify valid date
            booking_date = form.cleaned_data.get('booking_date')
            booking_time = form.cleaned_data.get('booking_time')
            tomorrow = datetime.date.today() + datetime.timedelta(days=1)
            if booking_date == datetime.date.today():
                error_message = f"Please call the restaurant \
                                  to make a booking for today.\n\
                                  Only bookings from {tomorrow} may be \
                                  made online."
                return render(
                              request,
                              'create_booking.html',
                              {'err_msg': True,
                               'error_message': error_message
                               }
                              )
            elif booking_date < datetime.date.today():
                error_message = f"Please enter a valid date. \
                                  Online bookings only from {tomorrow}."
                return render(
                              request,
                              'create_booking.html',
                              {'err_msg': True,
                               'error_message': error_message
                               }
                              )

            # Verify that the booking time is within business hours
            if booking_time.hour < 10 or booking_time.hour >= 21:
                error_message = "Kindly make a booking between 10am and 9pm!"
                return render(
                              request,
                              'create_booking.html',
                              {'err_msg': True,
                               'error_message': error_message
                               }
                              )

            # Verify that the table is not already booked
            table_id = form.cleaned_data.get('table_id')
            try:
                check_table = Table.objects.get(table_id=table_id)
                if check_table.open == 1:
                    try:
                        get_booking = Booking.objects.filter(
                            table_id=table_id,
                            booking_date=booking_date).first()
                        if get_booking:
                            error_message = f'Table "{table_id}" \
                                              is already booked.'
                            return render(
                                          request,
                                          'create_booking.html',
                                          {'err_msg': True,
                                           'error_message': error_message
                                           }
                                          )
                    except Booking.DoesNotExist:
                        return
            except Table.DoesNotExist:
                message = {
                           'err_msg': True,
                           'error_message': "Enter a valid table id."
                           }
                return render(request, 'create_booking.html', message)

            try:
                # save the form
                form = form.save(commit=False)
                form.login_email = request.user.email
                form.save()

                book_table(request, form.table_id)
                booking_id = form.booking_id
                booking_date = request.POST['booking_date']
                booking_time = request.POST['booking_time']
                no_of_guests = request.POST['no_of_guests']
                table_id = request.POST['table_id']
                user = request.user.username
                login_email = request.user.email
                email_to = settings.EMAIL_HOST_USER
                subject = "New booking from " + user
                body = (f"{user} made booking {booking_id} for "
                        f"{booking_date} at {booking_time} for "
                        f"{no_of_guests} guests, on table {table_id}")
                send_mail(subject, body, login_email, [email_to])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')

            if success_message == 'ON':
                return render(
                              request,
                              'create_booking.html',
                              {'message': 'Booking successful!'}
                              )
            else:
                messages.success(request, 'Booking successful!')
            return redirect('booking')

    form = BookingForm()
    context = {
        'form': form
    }
    return render(request, 'create_booking.html', context)


def update_booking(request, booking_id):
    """Provide a means for users to change bookings"""
    booking = get_object_or_404(Booking, booking_id=booking_id)
    init_table_id = booking.table_id
    init_booking_date = booking.booking_date
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            # verify valid date
            booking_date = form.cleaned_data.get('booking_date')
            booking_time = form.cleaned_data.get('booking_time')
            tomorrow = datetime.date.today() + datetime.timedelta(days=1)
            if booking_date == datetime.date.today():
                error_message = f"Please call the restaurant \
                                 to change a booking made for today.\n\
                                 Only bookings from {tomorrow} may be \
                                 changed online."
                return render(
                              request,
                              'update_booking.html',
                              {'err_msg': True,
                               'error_message': error_message
                               }
                              )
            elif booking_date < datetime.date.today():
                tomorrow = datetime.date.today() + datetime.timedelta(days=1)
                error_message = f"Please enter a valid date. \
                                  Online bookings only from {tomorrow}."
                return render(
                              request,
                              'update_booking.html',
                              {'err_msg': True,
                               'error_message': error_message
                               }
                              )

            # Verify that the booking time is within business hours
            if booking_time.hour < 10 or booking_time.hour >= 21:
                error_message = "Kindly make a booking between 10am and 9pm!"
                return render(
                              request,
                              'update_booking.html',
                              {'err_msg': True,
                               'error_message': error_message
                               }
                              )

            # Verify that the table is not already booked
            table_id = form.cleaned_data.get('table_id')
            if init_table_id != table_id or init_booking_date != booking_date:
                try:
                    check_table = Table.objects.get(table_id=table_id)
                    if check_table.open == 1:
                        error_message = f'Table "{table_id}" \
                                          is already booked.'
                        return render(
                                      request,
                                      'update_booking.html',
                                      {'err_msg': True,
                                       'error_message': error_message
                                       }
                                      )
                except Table.DoesNotExist:
                    message = {
                               'err_msg': True,
                               'error_message': "Enter a valid table id."
                               }
                    return render(request, 'update_booking.html', message)

            if form.cleaned_data.get('confirm') == 'Yes':
                booking = form.save(commit=False)
                booking.confirm = 'No'
                booking.save()
            else:
                form.save()

            if init_table_id != table_id:
                open_table(request, init_table_id)
                book_table(request, table_id)

            try:
                booking_date = form.cleaned_data.get('booking_date')
                booking_time = form.cleaned_data.get('booking_time')
                no_of_guests = form.cleaned_data.get('no_of_guests')
                user = request.user.username
                login_email = request.user.email
                email_to = settings.EMAIL_HOST_USER
                subject = "Booking change message from " + user
                body = (f"{user} has changed booking {booking_id} for "
                        f"{booking_date} at {booking_time} for "
                        f"{no_of_guests} guests, on table {table_id}")
                send_mail(subject, body, login_email, [email_to])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')

            if success_message == 'ON':
                return render(
                              request,
                              'update_booking.html',
                              {'message': 'Booking change successful!'}
                              )
            else:
                messages.success(request, 'Booking change successful!')
            return redirect('booking')

    form = BookingForm(instance=booking)
    context = {
        'form': form
    }
    return render(request, 'update_booking.html', context)


def delete_booking(request, booking_id):
    """Provide a means for users to delete bookings"""
    booking = get_object_or_404(Booking, booking_id=booking_id)
    booking.delete()
    try:
        open_table(request, booking.table_id)
        booking_date = booking.booking_date
        booking_time = booking.booking_time
        no_of_guests = booking.no_of_guests
        table_id = booking.table_id
        user = request.user.username
        login_email = request.user.email
        email_to = settings.EMAIL_HOST_USER
        subject = "Booking deleted by " + user
        body = (f"{user} has deleted booking {booking_id} for "
                f"{booking_date} at {booking_time} for "
                f"{no_of_guests} guests, on table {table_id}")
        send_mail(subject, body, login_email, [email_to])
    except BadHeaderError:
        return HttpResponse('Invalid header found.')

    messages.success(request, 'Booking deleted!')
    return redirect('booking')


def cancel_booking(request, booking_id):
    """Provide a means for users to cancel bookings"""
    booking = get_object_or_404(Booking, booking_id=booking_id)
    booking.confirm = 'Cancel'
    booking.save()
    try:
        open_table(request, booking.table_id)
        booking_date = booking.booking_date
        booking_time = booking.booking_time
        no_of_guests = booking.no_of_guests
        table_id = booking.table_id
        user = request.user.username
        login_email = request.user.email
        email_to = settings.EMAIL_HOST_USER
        subject = "Booking cancellation from " + user
        body = (f"{user} has cancelled booking {booking_id} for "
                f"{booking_date} at {booking_time} for "
                f"{no_of_guests} guests, on table {table_id}")
        send_mail(subject, body, login_email, [email_to])
    except BadHeaderError:
        return HttpResponse('Invalid header found.')

    messages.success(request, 'Booking cancelled!')
    return redirect('booking')


# The Tables Form section
def view_tables(request):
    """ View of Table table """
    tables = Table.objects.filter(open=0).order_by('table_id').all()
    # tables = Table.objects.order_by('table_id').all()
    context = {
        'tables': tables
    }
    return render(request, 'tables.html', context)


def book_table(request, table_id):
    """ This function sets open to 1 (booked) """
    table = get_object_or_404(Table, table_id=table_id)
    table.open = 1
    table.save()
    return redirect('booking')


def open_table(request, table_id):
    """ This function sets open to 0 (open) """
    table = get_object_or_404(Table, table_id=table_id)
    table.open = 0
    table.save()
    return redirect('booking')


def valid_dt(request, booking_date, booking_time):
    """ Validate date and time """
    if booking_time.hour < 10 or booking_time.hour >= 21:
        error_message = "Kindly make a booking between 10am and 9pm!"
        return render(
                      request,
                      'update_booking.html',
                      {'bus_hours': True,
                       'error_message': error_message
                       }
                      )

    if booking_date == datetime.date.today():
        error_message = "Please call the restaurant to book for today!"
        return render(
                      request,
                      'update_booking.html',
                      {'dt_today': True,
                       'error_message': error_message
                       }
                      )
    elif booking_date < datetime.date.today():
        tomorrow = datetime.date.today() + datetime.timedelta(days=1)
        error_message = f"Please enter a valid date, starting from {tomorrow}"
        return render(
                      request,
                      'update_booking.html',
                      {'dt_yday': True,
                       'error_message': error_message
                       }
                      )
    return True
