from typing import List
from ninja import Router

from rest_framework.exceptions import NotFound          

from travel.models import Agency, Trip
from travel.schemas import AgencyOut, TripsOut
from django.shortcuts import get_object_or_404




agency_router = Router(tags=["agencies"])


@agency_router.get("/all_agencies", response=List[AgencyOut])
def all_(request):
    agencies = Agency.objects.all()
    
    if not agencies:
        return "NO agency was FOUND"
    return agencies
    

@agency_router.get("/agency_trips", response=List[TripsOut])
def all_trips(request, id: int):
    
    agency = get_object_or_404(Agency, id=id)
    
    trips = agency.trips.all()
    
    if not trips:
        return "there are NO trips"
    return trips
    
  