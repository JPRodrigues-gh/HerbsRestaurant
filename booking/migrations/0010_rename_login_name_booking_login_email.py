# Generated by Django 3.2.15 on 2022-08-24 09:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0009_rename_login_id_booking_login_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='login_name',
            new_name='login_email',
        ),
    ]