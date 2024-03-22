from django.shortcuts import render

from rest_framework import viewsets
from .models import Booking
from .serializers import FlightBookingSerializer
# Create your views here.

class FlightBookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = FlightBookingSerializer
