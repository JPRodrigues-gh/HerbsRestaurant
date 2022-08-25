''' url.py file in the booking app folder '''
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.menu, name='menu'),
    path('contact/', views.add_contact, name='contact'),
    path('about/', views.about, name='about'),
    path('booking/', views.view_booking, name='booking'),
    path('create/', views.create_booking, name='create'),
    path('update/<booking_id>', views.update_booking, name='update'),
    path('delete/<booking_id>', views.delete_booking, name='delete'),
    path('cancel/<booking_id>', views.cancel_booking, name='cancel'),
]
