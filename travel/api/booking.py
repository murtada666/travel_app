from ninja import Router

from travel.schemas import BookingIn, MessageOut, TravelerIn
from travel.models import Booking, Traveler

booking_router = Router(tags=["Booking"])



@booking_router.post("booking/", response=MessageOut)
def booking(request, booking_in: TravelerIn):
    print(booking_in)
    Traveler.objects.create(
        first_name = booking_in.first_name,
        last_name = booking_in.last_name,
        phone = booking_in.phone,
    )
    
    return {"message": "Booking DONE"}
