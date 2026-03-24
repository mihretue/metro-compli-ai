from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from app.db.base import Base
from sqlalchemy.orm import relationship

class Building(Base):
    __tablename__ = "buildings"

    id = Column(Integer, primary_key=True, index=True)

    # Core identifiers
    bbl = Column(String, index=True, nullable=False)
    bin = Column(String, index=True, nullable=True)

    # Location info
    address = Column(String, nullable=True)
    borough = Column(String, nullable=True)

    # Physical attributes
    year_built = Column(Integer, nullable=True)
    gross_sqft = Column(Float, nullable=True)

    # CSV-derived/custom metrics
    cp0 = Column(Float, nullable=True)  # placeholder metric from your dataset

    created_at = Column(DateTime, default=datetime.utcnow)
    
    emissions = relationship("EmissionRecord", backref="building")
    assessments = relationship("ComplianceAssessment", backref="building")