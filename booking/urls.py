''' url.py file in the booking app folder '''
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.menu, name='menu'),
    path('contact/', views.add_contact, name='contact'),
    path('about/', views.about, name='about'),
    path('booking/', views.add_booking, name='booking'),
]
