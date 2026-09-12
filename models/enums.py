from enum import Enum
"""
This defines the enumerations used throughout the car rental system.

The enumerations provide predefined values for user roles, activation status,
and booking status.
"""
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
