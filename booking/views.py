from django.shortcuts import render
from django.views import generic
from .models import Booking


def index(request):
    return render(request, 'index.html')


# def menu(request):
#     return render(request, 'menu.html')


# def about(request):
#     return render(request, 'about.html')


# def store(request):
#     return render(request, 'store.html')


# class BookingList(generic.ListView):
#     """ View of Booking table """
#     model = Booking
#     queryset = Booking.objects.order_by('booking_date')
#     template_name = 'booking_detail.html'
#     paginate_by = 10
