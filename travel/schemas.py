from decimal import Decimal
from ninja import Schema


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
    