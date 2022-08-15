from django.shortcuts import render
from django.views import generic
from .models import Booking


class BookingList(generic.ListView):
    """ View of Booking table """
    model = Booking
    queryset = Booking.objects.order_by('booking_date')
    template_name = 'index.html'
    # paginate_by = 10
