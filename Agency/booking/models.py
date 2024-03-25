from django.db import models
from operator import mod
from datetime import datetime, timedelta 
from account.models import User
from flights.models import Flight,FlightSeatClass
# Create your models here.
'''
class Booking(models.Model):
    STATUS_CHOICES = (
        ('CNL', 'Canceled'),
        ('PPD', 'Postponed'),
        ('CMP', 'Completed'),
    )
    user = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    flight = models.ForeignKey(Flight,on_delete=models.SET_NULL,null=True)
    booking_date = models.DateTimeField(auto_now_add=True)
    seat_class = models.ForeignKey(FlightSeatClass, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='CMP')
    def __str__(self):
        return f'Booking {self.id} - User: {self.user.username} - Status: {self.get_status_display()}'
'''
class Booking(models.Model):
    TRIP_TYPE_CHOICES = (
        ('OW', 'One Way'),
        ('RT', 'Round Trip'),
    )
    STATUS_CHOICES = (
        ('CNL', 'Canceled'),
        ('PPD', 'Postponed'),
        ('CMP', 'Completed'),
    )
    booking_id= models.AutoField(primary_key=True,default=1)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    outbound_flight = models.ForeignKey(Flight, related_name='outbound_bookings', on_delete=models.SET_NULL, null=True)
    return_flight = models.ForeignKey(Flight, related_name='return_bookings', on_delete=models.SET_NULL, null=True, blank=True)
    booking_date = models.DateTimeField(auto_now_add=True)
    seat_class = models.ForeignKey(FlightSeatClass, on_delete=models.CASCADE)
    trip_type = models.CharField(max_length=2, choices=TRIP_TYPE_CHOICES, default='OW')
    status = models.CharField(max_length=3, choices=STATUS_CHOICES, default='CMP')

    def __str__(self):
        return f'Booking {self.id} - User: {self.user.username} - Status: {self.get_status_display()}'

        