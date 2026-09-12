
from dataclasses import dataclass, field
import uuid
from .enums import role as role,status
from models.BaseEntity import BaseEntity
from utils.password_utils import hash_password, verify_password

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

    def set_password(self, plain_password: str) -> None:
        self._password = hash_password(plain_password)

    def check_password(self, plain_password: str) -> bool:
        return bool(self._password) and verify_password(plain_password, self._password)


    def summary(self) -> str:
        role_label = self.role.value if hasattr(self.role, "value") else self.role
        return f"User: {self.name} ({role_label}) - {self.email}"
