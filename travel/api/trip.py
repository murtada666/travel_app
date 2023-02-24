from ninja import Router

from travel.models import Trip
from travel.schemas import TripDetailsOut

trip_router = Router(tags=["Trip"])


@trip_router.get("trip_details/", response=TripDetailsOut)
def trip_details(request, id: int):
    
    trip = Trip.objects.get(id=id)
    
    if not trip:
        return "trip NOT found"
    else:
        return trip