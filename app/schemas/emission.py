from pydantic import BaseModel
from typing import Optional

class EmissionCreate(BaseModel):
    building_bbl: str
    year: int
    emissions: Optional[float] = None
    energy_use: Optional[float] = None
    source: Optional[str] = "csv"