from typing import List
from ninja import Router

from travel.models import Agency, Trip
from travel.schemas import AgencyOut, TripsOut



agency_router = Router(tags=["agencies"])


@agency_router.get("/all_agencies", response=List[AgencyOut])
def all_(request):
    agencies = Agency.objects.all()
    
    if not agencies:
        return "NO agency was FOUND"
    else:
        return agencies
    

@agency_router.get("/agency_trips", response=List[TripsOut])
def all_trips(request, id: int):
    

    agency = Agency.objects.get(id=id)
    
    trips = agency.trips.all()

    return trips