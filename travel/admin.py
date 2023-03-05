from django.contrib import admin

from travel.models import *
# Register your models here.


admin.site.register(City)
admin.site.register(Country)
admin.site.register(Trip)
admin.site.register(Booking)
admin.site.register(Traveler)
admin.site.register(Agency)
# admin.site.register(Destination)