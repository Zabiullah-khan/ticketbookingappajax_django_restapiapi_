# Generated by Django 3.2.18 on 2023-06-28 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airbooking', '0006_passenger_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='passenger',
            name='seat_no',
            field=models.CharField(default='null', max_length=20),
        ),
    ]
