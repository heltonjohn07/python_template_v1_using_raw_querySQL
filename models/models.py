
from pydantic import BaseModel
from typing import List, Optional

class People(BaseModel):
    name: str
    email: Optional[str] = None
    whatsapp: Optional[str] = None
    city: Optional[str] = None
    uf: Optional[str] = None