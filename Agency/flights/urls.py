from django.urls import path,include
from . import views


urlpatterns = [
    path('flight/',views.get_all_flights,name='flight'),
    path('flight/<str:pk>/',views.get_by_id_flights, name='get_by_id_flights'),
    path('api/',views.get_all_flights,name='flight'),
             ]