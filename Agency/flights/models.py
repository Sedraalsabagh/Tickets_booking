from django.db import models
from account.models import User 
from datetime import timedelta,datetime
# Create your models here.



class Policy(models.Model):
    policy_id = models.IntegerField(default=1)
    refundable = models.BooleanField(default=False)
    exchangeable = models.BooleanField(default=False)
    exchangeable_condition = models.CharField(max_length=255, blank=True, null=True)
    cancellation_period = models.DurationField(default=0)

    def __str__(self):
        return str(self.policy_id)

class Airline (models.Model) :
   airline_id=models.IntegerField(default=0,blank=False)
   airline_name=models.CharField(max_length=100) 
   description=models.TextField(max_length=400)
   policy_id=models.ForeignKey(Policy,on_delete=models.CASCADE )  
   
   def __str__(self):
     return self.airline_name     

class Flight(models.Model):
    flight_id=models.IntegerField(blank=False)
    dateTime=models.DateTimeField(default=datetime.now)
    duration =models.DurationField(default=timedelta(days=0))
    airportDeparture=models.CharField(max_length=40)
    airportArrival=models.CharField(max_length=40)
    notes=models.TextField(max_length=200)
    total_rate=models.IntegerField(default=0)
    #user=models.ForeignKey(User,null=True,on_delete=models.SET_NULL)
    airline = models.ForeignKey(Airline, null=True, on_delete=models.SET_NULL)  
    departure_city = models.CharField(max_length=100,blank=False,null=False,default='unknow')
    destination_city = models.CharField(max_length=100,blank=False,null=False,default='unknow')
    departure_country = models.CharField(max_length=100,blank=False,null=False,default='unknow')
    destination_country = models.CharField(max_length=100,blank=False,null=False,default='unknow')
    def __str__(self):
      return str(self.duration)






class FlightSeatClass(models.Model):
    CLASS_CHOICES = (
        ('Economy', 'Economy'),
        ('Business Class', 'Business Class'),
        ('First Class', 'First Class'),
    )
    seats_type=models.IntegerField()
    flight=models.ForeignKey(Flight,on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=5)  
    capacity = models.IntegerField()
    def __str__(self):
      return self.seats_type



class Review(models.Model):
    flight_id=models.ForeignKey(Flight,null=True,on_delete=models.CASCADE,related_name='reviews')
    user=models.ForeignKey(User,null=True,on_delete=models.SET_NULL)
    comment=models.TextField(max_length=2000,default="",blank=False)
    ratings=models.IntegerField(default=0)
    createAt=models.DateTimeField(auto_now_add=True)
    def __str__(self):
      return str(self.ratings)