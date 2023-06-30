from django.contrib import admin
from .models import Passenger


# Register your models here.
@admin.register(Passenger)
class BookingAdmin(admin.ModelAdmin):
    class Meta:
        model = Passenger
        fields = "__all__"

