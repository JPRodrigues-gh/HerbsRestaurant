""" Add models to django admin """
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Table, User, Booking, Contact


@admin.register(Table, User, Booking, Contact)
class ContactAdmin(SummernoteModelAdmin):
    """ Add summernote field functionality to contact.body field"""
    summernote_fields = ('body')
