from dataclasses import dataclass, field
from models.enums import status as Status
import uuid
from models.BaseEntity import BaseEntity

"""
This is the base entity for cars.
The Car class contains the information of cars.
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