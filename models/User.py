"""
This is the base entity for users. 
Both customers and admins are users, but they have different roles and permissions. 
The User class contains the basic information needed for authentication and identification.
"""
from dataclasses import dataclass, field
import uuid
from .enums import role as role,status
from models.BaseEntity import BaseEntity
 
@dataclass
class User(BaseEntity):
    name: str
    email: str
    _password: str
    phone: str
    role: role
    loyal_point: float
    id: str = field(default_factory=lambda: str(uuid.uuid4())[:8])
    status: status = field(default=status.ACTIVE)
