from dataclasses import dataclass
from datetime import date
from models.BaseEntity import BaseEntity


@dataclass
class Booking(BaseEntity):
    id: str
    car_id: str
    user_id: str
    booking_no: str
    start_date: date
    end_date: date
    pick_up_date: date
    payment_date: date
    return_date: date
    rental_fee: float
    status: str