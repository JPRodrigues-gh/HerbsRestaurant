from django.shortcuts import render, redirect
from django.views import generic
from .models import Booking, Contact
from .contact import ContactForm


def index(request):
    return render(request, 'index.html')


def menu(request):
    return render(request, 'menu.html')


# The Contact Form section
def contact(request):
    return render(request, 'contact.html')


def get_contact(request):
    contacts = Contact.objects.all()
    context = {
        'contacts': contacts
    }
    return render(request, 'contact.html', context)


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
