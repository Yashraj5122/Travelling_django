from django.contrib import admin

from .models import Trip
from .models import Route

admin.site.register(Trip)
admin.site.register(Route)
