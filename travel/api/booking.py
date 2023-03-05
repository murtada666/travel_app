from ninja import Router

from travel.schemas import MessageOut, TravelerIn
from travel.models import Traveler

booking_router = Router(tags=["Booking"])



@booking_router.post("booking/", response={200:MessageOut})
def booking(request, booking_in: TravelerIn):

    Traveler.objects.create(
        first_name = booking_in.first_name,
        last_name = booking_in.last_name,   
        phone = booking_in.phone,
        age = booking_in.age,
    )
    
<<<<<<< HEAD
    return {"message": "Booking DONE"}
=======
    return 200, {"message": "Booking DONE"}
>>>>>>> 26e70805d368b54ebe75d4283e96190aa6afd38d
