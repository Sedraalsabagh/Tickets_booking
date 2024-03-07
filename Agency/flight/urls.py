from django.urls import path
from . import views

urlpatterns=[
   path('flight',views.get_all_flight,name='flights') ,
   path('flight/<str:pk>/',views.get_by_id_flight, name='get_by_id_flight') ,
   

]