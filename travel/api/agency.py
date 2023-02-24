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
    

@agency_router.get("/agency_trips", response=TripsOut)
def all_trips(request, agency_name: str):
    
    agency = Agency.objects.get(name=agency_name)
    
    trips = agency.trips.all()
#------------------------------------------------------------------------

    # trips = Agency.objects.get(name=agency_name).trips.all()
    
    
#------------------------------------------------------------------------
    
    # trips = Trip.objects.filter(agency=Agency.objects.get(name=agency_name))
    
    # print(Agency.objects.get(name=agency_name))
    
#------------------------------------------------------------------------
    
    # trips = agency.trip_set.all()
    # print(trips)
    
    return trips