from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey, String
from datetime import datetime
from app.db.base import Base

class EmissionRecord(Base):
    __tablename__ = "emission_records"

    id = Column(Integer, primary_key=True, index=True)

    building_id = Column(Integer, ForeignKey("buildings.id"), index=True)

    year = Column(Integer, index=True)

    emissions = Column(Float, nullable=True)     # CO2 equivalent
    energy_use = Column(Float, nullable=True)

    source = Column(String, nullable=True)  # CSV, API, manual

    created_at = Column(DateTime, default=datetime.utcnow)