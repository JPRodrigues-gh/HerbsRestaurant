''' url.py file in the booking app folder '''
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.menu, name='menu'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('booking/', views.BookingList.as_view(), name='booking'),
]
