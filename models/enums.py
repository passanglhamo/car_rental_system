from enum import Enum

class role(Enum):
    SYSTEM_ADMIN = "sadmin" #System Administrator
    ADMIN = "admin"
    CUSTOMER = "customer"

class status(Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"

class booking_status(Enum):
    PENDING = "PENDING"
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"
    RETURNED = "RETURNED"
    CANCELLED = "CANCELLED"   
