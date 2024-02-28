from django.db import models

class Booking(models.Model):
    ticket_id = models.CharField(primary_key=True,max_length=10)
    trip_id = models.CharField(max_length=100)
    traveller_name = models.CharField(max_length=100)
    traveller_number = models.CharField(max_length=100)
    ticket_cost = models.DecimalField(max_digits=10,decimal_places=2)
    traveller_email = models.EmailField()
