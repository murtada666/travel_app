from typing import List
from ninja import Router

from travel.models import City
from travel.schemas import CityOut, CityTripsOut
from django.shortcuts import get_object_or_404



city_router = Router(tags=["City"])



@city_router.get("all_cities/", response=List[CityOut])
def city_trips(request):
    
    city = City.objects.all()
    
    if not city:
        return "NO cities were FOUND"
    else:
        return city
    
    
    
@city_router.get("city_trips/", response=List[CityTripsOut])
def city_trips(request, id: int):
    
    city = get_object_or_404(City, id=id)
    
    trips = city.trips.all()
        
    if not trips:
        return "NO trips were FOUND"
    return trips