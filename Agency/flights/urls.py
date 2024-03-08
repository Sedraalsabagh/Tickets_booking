from django.urls import path
from . import views

urlpatterns = [
    path('flight/',views.get_all_flights,name='flight'),
    path('flight/',include('flights.urls')),
    path('flight/<str:pk>',views.get_by_id_flights,name='get_by_id_flight')


]