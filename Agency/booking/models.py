from django.db import models
from operator import mod
from account.models import User
from flight.models import Flight
# Create your models here.

class Booking(models.Model):
    STATUS_CHOICES = (
        ('CNL', 'Canceled'),
        ('PPD', 'Postponed'),
        ('CMP', 'Completed'),
    )
    user = models.ForeignKey(User, on_delete=models.SET_NULL)
    flight_id = models.ForeignKey(Flight,on_delete=models.SET_NULL)
    booking_date = models.DateTimeField(auto_now_add=True)
    seat_class = models.ForeignKey(FlightSeatClass, on_delete=models.CASCADE)
    
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='CMP')
    def __str__(self):
        return f'Booking {self.id} - User: {self.user.username} - Status: {self.get_status_display()}'