from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/booking/', views.booking_listing, name='booking_listing'),
    path('api/booking/<str:ticket_id>/', views.booking_details, name='booking_details'),
]
