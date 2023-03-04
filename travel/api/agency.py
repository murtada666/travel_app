from typing import List
from ninja import Router

from travel.models import Agency, Trip
from travel.schemas import AgencyOut, TripsOut, MessageOut
from django.shortcuts import get_object_or_404




agency_router = Router(tags=["agencies"])


@agency_router.get("/all_agencies", response={200:List[AgencyOut], 404:MessageOut, 500:MessageOut, 400:MessageOut})
def all(request):
    agencies = Agency.objects.all()

    if len(agencies) == 0:
        return 404, {'message': "NO agency was FOUND"}
    return agencies


@agency_router.get("/agency_trips", response=List[TripsOut])
def all_trips(request, id: int):

    agency = get_object_or_404(Agency, id=id)

    trips = agency.trips.all()

    if len(trips) == 0:
        return 404, {'message':"NO trips were FOUND"}
    return trips


