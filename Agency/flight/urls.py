from django.urls import path
from . import views

urlpatterns=[
    path('flight/',views.get_all_flight,name='flight'),
    path('flight/<str:pk>',views.get_by_id_flight,name='get_by_id_flight'),
    path('<str:pk>/reviews',views.create_review_review,name='create_review'),
    path('<str:pk>/reviews/delete',views.delete_review_review,name='delete_review'),

]
