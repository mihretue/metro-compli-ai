from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.building import Building
from app.services.compliance_service import calculate_compliance

router = APIRouter(
    tags=["Compliance"]
)


@router.get("/buildings/{bbl}/compliance/{year}")
def check_compliance(bbl:str,year:int,db:Session = Depends(get_db)):
    building = db.query(Building).filter(
        Building.bbl == bbl
    ).first()
    
    if not building:
        raise HTTPException(status_code=400,detail="Building not found")
    result = calculate_compliance(db,building=building,year=year)
    
    if not result:
        raise HTTPException(status_code=404, detail="Missing data or rule")
    
    return {
        "bbl": bbl,
        "year": year,
        **result
    }