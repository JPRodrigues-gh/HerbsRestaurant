""" Add models to django admin """
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Table, User, Booking, Contact


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    """ Add filter functionality to Table table on open and table_size"""
    list_filter = ('open', 'table_size',)


@admin.register(User, Contact)
class ContactAdmin(SummernoteModelAdmin):
    """ Add summernote field functionality to contact.body field"""
    list_filter = ('name', 'surname', 'created_date',)
    summernote_fields = ('body')


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    """ Add filter functionality to Booking table on booking_date"""
    list_filter = ('booking_date',)
