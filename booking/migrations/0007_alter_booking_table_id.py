# Generated by Django 3.2.15 on 2022-12-08 11:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0006_alter_booking_table_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='table_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='booking.table'),
        ),
    ]
