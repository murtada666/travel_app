from decimal import Decimal
from ninja import Schema


class MessageOut(Schema):
    message: str


class AgencyOut(Schema):
    id: int
    name: str
    logo: str
    
    
class TripsOut(Schema):
    id: int
    agency: AgencyOut
    name: str
    price: Decimal
    image: str
    
    
class DestinationOut(Schema):
    id: int
    name: str
    image: str
    
    
class DestinationTripsOut(Schema):
    id: int
    image: str
    name: str
    price: Decimal
    
    
    
class DestinationName(Schema):
    id: int
    name:str
class TripDetailsOut(Schema):
    id: int
    image: str
    price: Decimal
    destination: DestinationName
    # departure_date: str
    description: str
    
    
class TravelerIn(Schema):
    first_name: str
    last_name: str
    phone: int 
class BookingIn(Schema):
    traveler: TravelerIn
    
    