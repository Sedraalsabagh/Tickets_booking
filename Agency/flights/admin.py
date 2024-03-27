from django.contrib import admin
from .models import Flight,Airline,Policy,FlightSeatClass,FlightSchedule,RefundedPayment,Airport
# Register your models here.

admin.site.register(Flight)
admin.site.register(Airline)
admin.site.register(Policy)
admin.site.register(FlightSeatClass)
admin.site.register(RefundedPayment)
admin.site.register(FlightSchedule)
admin.site.register(Airport)





