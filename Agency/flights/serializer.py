from rest_framework import serializers
from .models import Flight,Review,Airline
from rest_framework_simplejwt.tokens import AccessToken

class FlightSerializer(serializers.ModelSerializer) :
    
    class Meta:
        model=Flight
        fields=['departure_date','airportDeparture','airportArrival','departure_city','destination_city','departure_country','return_date','duration','notes','ratings']
    '''
    def get_reviews(self,obj):
        reviews=obj.reviews.all()
        serializer=ReviewSerializer(reviews,many=True)
        return serializer.data
    '''
class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model=Review
        fields="__all__"

