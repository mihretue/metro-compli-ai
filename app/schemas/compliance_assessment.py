from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ComplianceAssessmentBase(BaseModel):
    building_id: int
    year: int

    predicted_emissions: Optional[float] = None
    actual_emissions: Optional[float] = None

    estimated_fine: Optional[float] = None
    compliance_status: Optional[str] = None

class ComplianceAssessmentCreate(ComplianceAssessmentBase):
    pass
    
    
class ComplianceAssessmentResponse(ComplianceAssessmentBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True  # allows ORM → Pydantic conversion