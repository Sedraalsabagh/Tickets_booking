from rest_framework import serializers
from .models import Booking

class FlightBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
