from sqlalchemy import Column, Integer, Float, String, ForeignKey, DateTime
from datetime import datetime
from app.db.base import Base

class ComplianceAssessment(Base):
    __tablename__ = "compliance_assessments"

    id = Column(Integer, primary_key=True, index=True)

    building_id = Column(Integer, ForeignKey("buildings.id"), index=True)

    year = Column(Integer, index=True)

    predicted_emissions = Column(Float)
    actual_emissions = Column(Float)

    estimated_fine = Column(Float)

    compliance_status = Column(String)  # compliant, at-risk, non-compliant

    created_at = Column(DateTime, default=datetime.utcnow)