from typing import List
from ninja import Router

from travel.models import Agency
from travel.schemas import AgencyOut



agency_router = Router(tags=["agencies"])


@agency_router.get("/all_agencies", response=List[AgencyOut])
def all_(request):
    agencies = Agency.objects.all()
    
    if not agencies:
        return "NO agency was FOUND"
    else:
        return agencies
    

@agency_router.get("/agency_trips")
def all_trips(request, agency_name: str):
    agency = Agency.objects.filter(name=agency_name).all()
    
    trips = agency.trips.all()
    
    return trips