
from dataclasses import dataclass, field
import uuid
from .enums import role as role,status
from models.BaseEntity import BaseEntity
"""
    This is entity which contain user's information.

    The User class stores personal information, authentication details,
    user role, and loyalty points.

    Attributes:
        name (str): Full name of the user.
        email (str): Email address used to identify and contact the user.
        _password (str): Hashed password used for user authentication.
        phone (str): Contact phone number of the user.
        role (role): Role assigned to the user, such as System Administrator,
            Administrator, or Customer.
        loyal_point (float): Number of loyalty points accumulated by the user.
        id (str): Unique identifier automatically generated for the user.
"""      
@dataclass
class User(BaseEntity):
    name: str
    email: str
    _password: str
    phone: str
    role: role
    loyal_point: int
    id: str = field(default_factory=lambda: str(uuid.uuid4())[:8])
    status: status = field(default=status.ACTIVE)
