from ninja import Router
from django.shortcuts import get_object_or_404
from travel.models import Trip
from travel.schemas import TripDetailsOut

trip_router = Router(tags=["Trip"])


@trip_router.get("trip_details/", response={200:TripDetailsOut})
def trip_details(request, id: int):
    
    trip = get_object_or_404(Trip, id=id)
    
    return trip
