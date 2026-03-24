from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
import pandas as pd
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.building import Building
from app.models.emission_record import EmissionRecord
from app.schemas.building import BuildingResponse
from typing import List

router = APIRouter(
    tags=["uploads"]
)


def get_or_create_building(db: Session, bbl: str, row: dict):
    building = db.query(Building).filter(Building.bbl == bbl).first()

    if building:
        return building

    building = Building(
        bbl=bbl,
        bin=row.get("BIN"),
        address=row.get("Address"),
        borough=row.get("Borough"),
        year_built=row.get("YearBuilt"),
        gross_sqft=row.get("GrossSqft"),
        cp0=row.get("CP0"),
    )

    db.add(building)
    db.flush()  # get ID without commit
    return building



@router.post("/upload-csv")
async def upload_csv(file: UploadFile = File(...), db: Session = Depends(get_db)):
    if not file.filename.endswith(".csv"):
        raise HTTPException(status_code=400, detail="Only CSV files allowed")

    try:
        df = pd.read_csv(file.file)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Invalid CSV: {str(e)}")

    required_columns = ["BBL"]

    for col in required_columns:
        if col not in df.columns:
            raise HTTPException(status_code=400, detail=f"Missing column: {col}")

    inserted_buildings = 0
    inserted_emissions = 0

    for _, row in df.iterrows():
        row_dict = row.to_dict()

        bbl = str(row_dict.get("BBL"))

        building = get_or_create_building(db, bbl, row_dict)
        inserted_buildings += 1

        # Emissions (if present in CSV)
        if "Year" in row_dict and "Emissions" in row_dict:
            emission = EmissionRecord(
                building_id=building.id,
                year=int(row_dict.get("Year")),
                emissions=row_dict.get("Emissions"),
                energy_use=row_dict.get("EnergyUse"),
                source="csv"
            )
            db.add(emission)
            inserted_emissions += 1

    db.commit()

    return {
        "message": "CSV processed successfully",
        "buildings_processed": inserted_buildings,
        "emissions_inserted": inserted_emissions
    }
    
    
    
@router.get("/buildings",response_model=List[BuildingResponse])
def get_building(db:Session = Depends(get_db)):
    buildings = db.query(Building).all()
    
    return buildings
