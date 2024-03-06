from django.db import models

# Create your models here.

from django.db import models
from datetime import timedelta

  
class Policy(models.Model) :
    policy_id=models.IntegerField(max_length=10,blank=False)
    refundable=models.BooleanField(default=False,blank=False)
    exchangeable=models.BooleanField(default=False,blank=False)
    exchangeable_condation=models.TextField(default=False,blank=False)
    cancellationPeriod=models.DurationField(default=timedelta(days=0))
    def str(self):
        return self.policy_id
        
    
class Airline (models.Model) :
   airline_id=models.IntegerField(max_length=10,blank=False)
   airline_name=models.CharField(max_length=20) 
   description=models.TimeField(max_length=400)
   policy_id=models.ForeignKey(Policy,on_delete=models.CASCADE)  
   def str(self):
     return self.airline_name