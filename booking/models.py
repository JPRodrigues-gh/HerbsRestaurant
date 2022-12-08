""" models.py contains models for the DB objects"""
from django.db import models

OPEN = ((0, "Open"), (1, "Booked"))
CONFIRM = ((0, "No"), (1, "Yes"))
TABLE_SIZES = ((2, "2-Places"), (4, "4-Places"), (6, "6-Places"),
               (8, "8-Places"))


class Table(models.Model):
    """ Model for the Tables table """
    table_id = models.CharField(max_length=30, unique=True)
    no_of_places = models.IntegerField()
    open = models.IntegerField(choices=OPEN, default=0)
    table_size = models.IntegerField(choices=TABLE_SIZES)

    class Meta:
        """ Order the Tables listing by table_id ascending"""
        ordering = ['table_id']

    def __str__(self):
        return str(self.table_id)

    def number_of_open(self):
        """ Fetch a count of open tables """
        return self.open.filter(1).count()


class User(models.Model):
    """ Model for the users table """
    user_id = models.BigAutoField(
        auto_created=True,
        primary_key=True,
        serialize=False,
        verbose_name='ID')
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    login_id = models.CharField(max_length=50, blank=True)
    address1 = models.CharField(max_length=50, blank=True)
    address2 = models.CharField(max_length=50, blank=True)
    address3 = models.CharField(max_length=50, blank=True)
    postal_code = models.CharField(max_length=50, blank=True)
    town_city = models.CharField(max_length=50, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)


class Booking(models.Model):
    """ Model for the bookings table """
    booking_id = models.BigAutoField(
        auto_created=True,
        primary_key=True,
        serialize=False,
        verbose_name='ID')
    booking_date = models.DateField()
    booking_time = models.TimeField()
    created_date = models.DateTimeField(auto_now_add=True)
    last_updated_on = models.DateTimeField(auto_now=True)
    table_id = models.ForeignKey(Table, on_delete=models.PROTECT)
    no_of_guests = models.PositiveIntegerField()
    confirm = models.CharField(max_length=10, default='No')
    login_email = models.CharField(max_length=50)

    class Meta:
        """ Order the bookings by date ascending"""
        ordering = ['booking_date']

    def __str__(self):
        return str(self.booking_id)


class BookingJoin(models.Model):
    """
    Model holds information that connects a user
    and tables booked to a unique booking id
    """
    booking_id = models.ForeignKey(Booking, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    table_id = models.ForeignKey(Table, on_delete=models.CASCADE)


class Contact(models.Model):
    """ Model for the contact table """
    contact_id = models.BigAutoField(
        auto_created=True,
        primary_key=True,
        serialize=False,
        verbose_name='ID')
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    phone = models.CharField(max_length=30, null=True, blank=True)
    email = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    body = models.TextField(max_length=250)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"from {self.name} {self.surname}, Comment {self.body}"
