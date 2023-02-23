from ninja import Router

booking_router = Router(tags=["Booking"])



@booking_router.post("booking/")
def booking(request):
    pass