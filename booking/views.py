from django.shortcuts import render, redirect
from django.conf import settings
from django.core.mail import send_mass_mail, BadHeaderError
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
def contact(request):
    return render(request, 'contact.html')


def get_contact(request):
    form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def add_contact(request):
    """Provide a means for users to add items"""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            try:
                name = request.POST['name']
                subject = "Message from " + name
                email = request.POST['email']
                body = request.POST['body']
                email_from = settings.EMAIL_HOST_USER
                datatuple = (
                    (subject, body, email_from, [email]),
                    (subject, body, email_from, [email_from,]),
                )
                # send_mail(subject, body, email_from, [email], fail_silently=False)
                send_mass_mail(datatuple, fail_silently=False)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
    form = ContactForm()
    context = {
        'form': form
    }
    return render(request, 'contact.html', context)


def not_contact(request):
    # contacts = Contact.objects.all()

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})


def post_contact(request):
    if request.method == 'POST':
        name = request.POST.get('first_name')
        surname = request.POST.get('last_name ')
        phone = request.POST.get('cellphone_number')
        email = request.POST.get('email')
        cc = request.POST.get('cc')
        body = request.POST.get('add_info')
        Contact.objects.create(name=name, surname=surname, phone=phone, email=email, body=body)
        return redirect('contact')
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')


class BookingList(generic.ListView):
    """ View of Booking table """
    model = Booking
    queryset = Booking.objects.order_by('booking_date')
    template_name = 'booking_detail.html'
    # paginate_by = 10
