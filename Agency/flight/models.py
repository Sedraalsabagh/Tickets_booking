from django.db import models
from datetime import timedelta,datetime

from airline.models import Airline

# Create your models here.

class Flight(models.Model):
    flight_id=models.IntegerField(max_length=10,blank=False)
    id_airline=models.ForeignKey(Airline,on_delete=models.CASCADE)
    dateTime=models.DateTimeField(default=datetime.now)
    duration =models.DurationField(default=timedelta(days=0))
    airportDeparture=models.CharField(max_length=40)
    airportArrival=models.CharField(max_length=40)
    notes=models.TextField(max_length=200)
    total_rate=models.IntegerField(default=0)
    def __str__(self):
      return self.flight_id
      


class FlightSeatClass(models.Model):
    seats_type=models.IntegerField()
    flight_id=models.ForeignKey(Flight,on_delete=models.CASCADE)
    price=models.FloatField(max_length=100)
    count=models.IntegerField(max_length=100)
    def __str__(self):
      return self.seats_type



