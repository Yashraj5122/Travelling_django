# trip/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/trips/', views.trip_listing, name='trip_listing'),
    path('api/trips/<str:trip_id>/', views.trip_details, name='trip_details'),
]
