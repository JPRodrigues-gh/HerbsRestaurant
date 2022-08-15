''' url.py file in the booking app folder '''
from . import views
from django.urls import path


urlpatterns = [
    path('', views.BookingList.as_view(), name='home')
]
