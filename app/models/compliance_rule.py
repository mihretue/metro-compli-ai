from sqlalchemy import Column, Integer, String, Float
from app.db.base import Base

class ComplianceRule(Base):
    __tablename__ = "compliance_rules"

    id = Column(Integer, primary_key=True, index=True)

    building_type = Column(String, index=True)  # residential, commercial, etc.
    year = Column(Integer, index=True)

    emission_limit = Column(Float)  # threshold
    penalty_per_ton = Column(Float)