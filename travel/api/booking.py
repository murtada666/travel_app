from ninja import Router

from travel.schemas import BookingIn, MessageOut
from travel.models import Booking

booking_router = Router(tags=["Booking"])



@booking_router.post("booking/", response=MessageOut)
def booking(request, booking_in: BookingIn):
    
    Booking.objects.create(
        first_name = booking_in.traveler.first_name,
        last_name = booking_in.traveler.last_name,
        phone = booking_in.traveler.phone,
    )
    return {"message": "Booking DONE"}