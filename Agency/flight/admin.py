from django.contrib import admin
from .models import Flight,FlightSeatClass


# Register your models here.

admin.site.register(Flight)
admin.site.register(FlightSeatClass)

