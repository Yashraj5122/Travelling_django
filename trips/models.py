from django.db import models

class Trip(models.Model):
    trip_id = models.CharField(primary_key=True,max_length=10)
    user_id = models.IntegerField()
    vehicle_id = models.CharField(max_length=100)
    route_id = models.CharField(max_length=10)
    driver_name = models.CharField(max_length=100)
    trip_distance = models.FloatField()

class Route(models.Model):
    route_id = models.CharField(primary_key=True,max_length=10)
    user_id = models.IntegerField()
    route_name = models.CharField(max_length=100)
    route_origin = models.CharField(max_length=100)
    route_destination = models.CharField(max_length=100)
    stops = models.JSONField()
