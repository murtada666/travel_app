from decimal import Decimal
from ninja import Schema


class AgencyOut(Schema):
    id: int
    name: str
    logo: str
    
    
class TripOut(Schema):
    id: int
    name: str
    departure_date: int
    return_date: int