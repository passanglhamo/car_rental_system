from dataclasses import dataclass,field
from datetime import date
from typing import Optional


@dataclass
class BaseEntity:
    created_by: str
    created_date: date
    updated_by: Optional[str] = field(default=None, kw_only=True)
    updated_date: Optional[date] = field(default=None, kw_only=True)