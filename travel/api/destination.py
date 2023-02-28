from typing import List
from ninja import Router

from travel.models import Destination
from travel.schemas import DestinationOut, DestinationTripsOut
from django.shortcuts import get_object_or_404



destination_router = Router(tags=["Destination"])



@destination_router.get("all_destinations/", response=List[DestinationOut])
def destination_trips(request):
    
    destination = Destination.objects.all()
    
    if not destination:
        return "NO agency was FOUND"
    else:
        return destination
    
    
    
@destination_router.get("destination_trips/", response=List[DestinationTripsOut])
def destinations_trips(request, id: int):
    
    destination = get_object_or_404(Destination, id=id)
    
    trips = destination.trips.all()
        
    if not trips:
        return "NO trips were FOUND"
    return trips