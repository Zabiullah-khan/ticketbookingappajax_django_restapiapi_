# Generated by Django 3.2.18 on 2023-06-28 13:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('airbooking', '0003_passenger_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='passenger',
            name='date',
        ),
    ]
