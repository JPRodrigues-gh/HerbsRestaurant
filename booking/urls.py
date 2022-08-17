''' url.py file in the booking app folder '''
from django.urls import path
from . import views


urlpatterns = [
    # path('', views.BookingList.as_view(), name='index')
    path('', views.index, name='index')
]
