from dataclasses import dataclass
from datetime import date
from models.BaseEntity import BaseEntity

"""
    This  is entity which contain car rental booking made by a user.

    Attributes:
        id (str): Unique identifier for the booking.
        car_id (str): ID of the car associated with the booking.
        user_id (str): ID of the user who made the booking.
        booking_no (str): Unique booking reference number.
        start_date (date): Date when the rental period starts.
        end_date (date): Date when the rental period ends.
        pick_up_date (date): Date when the customer picks up the car.
        payment_date (date): Date when the rental payment is made.
        return_date (date): Date when the car is returned.
        rental_fee (float): Total rental fee for the booking.
        status (str): Status of the booking, such as
            Pending, Approved, Rejected, Cancelled and Returned.
"""
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