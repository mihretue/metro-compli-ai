from pydantic import BaseModel
from typing import Optional

# ✅ Base schema (shared fields)
class ComplianceRuleBase(BaseModel):
    building_type: str
    year: int
    emission_limit: float
    penalty_per_ton: float


# ✅ Create schema
class ComplianceRuleCreate(ComplianceRuleBase):
    pass


# ✅ Update schema
class ComplianceRuleUpdate(BaseModel):
    building_type: Optional[str] = None
    year: Optional[int] = None
    emission_limit: Optional[float] = None
    penalty_per_ton: Optional[float] = None


# ✅ Response schema
class ComplianceRuleResponse(ComplianceRuleBase):
    id: int

    class Config:
        from_attributes = True