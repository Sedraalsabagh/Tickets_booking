from django.contrib import admin
from .models import Flight,Airline#,FlightSeatClass
# Register your models here.

admin.site.register(Flight)
admin.site.register(Airline)

#admin.site.register(FlightSeatClass)




