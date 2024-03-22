from rest_framework import serializers
from .models import Booking

class FlightBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
        #fields = ['id', 'user', 'flight_id', 'booking_date', 'seat_class', 'status']