""" Configure project apps """
from django.apps import AppConfig


class BookingConfig(AppConfig):
    """ Defines the booking app"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'booking'
