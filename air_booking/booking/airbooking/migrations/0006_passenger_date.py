# Generated by Django 3.2.18 on 2023-06-28 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airbooking', '0005_alter_passenger_sex'),
    ]

    operations = [
        migrations.AddField(
            model_name='passenger',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]