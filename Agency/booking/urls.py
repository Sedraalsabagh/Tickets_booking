from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookingView

urlpatterns = [
path('bookings/', BookingView.as_view(), name='create_booking'),
]
