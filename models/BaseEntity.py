from dataclasses import dataclass,field
from datetime import date
from typing import Optional
"""
    This is base entity containing common audit fields shared by application entities.

    Attributes:
        created_by (str): User id of the user who created the entity.
        created_date (date): Date when the entity was created.
        updated_by (Optional[str]): User id of the user who last updated
            the entity. Defaults is None.
        updated_date (Optional[date]): Date when the entity was last updated.
            Defaults is None.
"""
@dataclass
class BaseEntity:
    created_by: str
    created_date: date
    updated_by: Optional[str] = field(default=None, kw_only=True)
    updated_date: Optional[date] = field(default=None, kw_only=True)