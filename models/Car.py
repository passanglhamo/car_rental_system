from dataclasses import dataclass, field
from models.enums import status as Status
import uuid
from models.BaseEntity import BaseEntity

"""
    This is entity which contain car's information.

    The Car class contains information about the car,
    rental pricing, rental period limits, and availability status.

    Attributes:
        make (str): Manufacturer or brand of the car.
        model (str): Model name of the car.
        year (int): Manufacturing year of the car.
        mileage (float): Current mileage of the car.
        daily_rate (float): Rental cost per day.
        min_period (int): Minimum number of days the car can be rented.
        max_period (int): Maximum number of days the car can be rented.
        status (Status): Activation status, such as Active and Inactive.
        id (str): Unique identifier automatically generated for the car.
"""
@dataclass
class Car(BaseEntity):
    make: str
    model: str
    year: int
    mileage: float
    daily_rate: float
    min_period: int
    max_period: int
    status: Status = Status.ACTIVE.value
    id: str = field(default_factory=lambda: str(uuid.uuid4())[:8])