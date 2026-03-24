from pydantic import BaseModel
from typing import Optional

class BuildingCreate(BaseModel):
    bbl: str
    bin: Optional[str] = None
    address: Optional[str]= None
    borough:Optional[str] = None
    year_built: Optional[int] = None
    gross_sqft: Optional[float] = None
    cp0: Optional[float] = None