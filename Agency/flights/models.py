from django.db import models
from account.models import User 
from datetime import timedelta,datetime
#from booking.models import Booking
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
    departure_date=models.DateField(default=datetime.now)
    return_date=models.DateField(default=datetime.now)
    duration =models.DurationField(default=timedelta(days=0))
    airportDeparture=models.CharField(max_length=40,blank=False,null=False)
    airportArrival=models.CharField(max_length=40,blank=False,null=False)
    notes=models.TextField(max_length=200,blank=True,null=True)
    ratings=models.IntegerField(blank=True, null=True)
    user=models.ForeignKey(User,null=True,on_delete=models.SET_NULL)
    departure_city = models.CharField(max_length=100,null=True,default='')
    destination_city = models.CharField(max_length=100,blank=False,null=False,default='')
    departure_country = models.CharField(max_length=100,blank=False,null=False,default='')
    destination_country = models.CharField(max_length=100,blank=False,null=False,default='')
    def __str__(self):
      return str(self.id)

class FlightSeatClass(models.Model):
    CLASS_CHOICES = (
        ('Economy', 'Economy'),
        ('Business Class', 'Business Class'),
        ('First Class', 'First Class'),
    )
    seats_type=models.CharField(max_length=20)
    flight=models.ForeignKey(Flight,on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=5)  
    capacity = models.IntegerField()
    def __str__(self):
      return self.seats_type



class Airport(models.Model):
    airport_id = models.AutoField(primary_key=True)
    airport_name = models.CharField(max_length=100)
    IATA_code = models.CharField(max_length=3)
    contact_info = models.TextField()
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.airport_name


class FlightSchedule(models.Model):
    id = models.AutoField(primary_key=True)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    airport = models.ForeignKey(Airport, on_delete=models.CASCADE)
    duration = models.DurationField()

    def __str__(self):
        return f"{self.flight} - {self.airport}"



#from booking.models import Booking

class RefundedPayment(models.Model):
    id = models.AutoField(primary_key=True)
    booking_id = models.ForeignKey('booking.Booking', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    notes = models.TextField()

    def __str__(self):
        return f"Refund for booking {self.booking_id} - Amount: {self.amount}"

class Review(models.Model):
    flight_id=models.ForeignKey(Flight,null=True,on_delete=models.CASCADE,related_name='reviews')
    user=models.ForeignKey(User,null=True,on_delete=models.SET_NULL)
    comment=models.TextField(max_length=2000,default="",blank=False)
    ratings=models.IntegerField(default=0)
    createAt=models.DateTimeField(auto_now_add=True)
    def __str__(self):
      return str(self.ratings)