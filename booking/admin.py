""" Add models to django admin """
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Table, User, Booking, Contact


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    """ Add filter functionality to Table table on open and table_size"""
    list_display = ('table_id', 'no_of_places', 'open', 'table_size',)
    list_filter = ('open', 'table_size',)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """ Add filter functionality to User"""
    search_fields = ('name', 'surname', 'created_date',)
    list_display = ('user_id', 'name', 'surname', 'phone', 'email')
    list_filter = ('name', 'surname', 'created_date',)


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    """ Add filter functionality to Booking table on booking_date"""
    list_display = (
        'booking_id',
        'booking_date',
        'booking_time',
        'no_of_guests',
        'login_email',
        'confirm')
    list_filter = ('booking_date',)
    actions = ['confirm_booking', 'unconfirm_booking', 'cancel_booking']

    def confirm_booking(self, queryset):
        """ Admin can confirm the booking """
        queryset.update(confirm='Yes')

    def unconfirm_booking(self, queryset):
        """ Admin can unconfirm the booking """
        queryset.update(confirm='No')

    def cancel_booking(self, queryset):
        """ Admin can cancel the booking """
        queryset.update(confirm='cancel')


@admin.register(Contact)
class ContactAdmin(SummernoteModelAdmin):
    """ Add summernote field functionality to contact.body field"""
    list_display = ('name', 'surname', 'phone', 'email', 'body', 'created_date',)
    list_filter = ('name', 'surname', 'created_date',)
    summernote_fields = ('body')
