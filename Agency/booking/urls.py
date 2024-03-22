from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FlightBookingViewSet

router = DefaultRouter()
router.register('flight-bookings', FlightBookingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
