from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.compliance_rule import ComplianceRule
from app.schemas.rule import ComplianceRuleCreate, ComplianceRuleResponse
from typing import List
router = APIRouter(
    prefix="/rules",
    tags=["Compliance Rules"]
)

@router.post("/", response_model=ComplianceRuleResponse)
def create_rule(rule_data: ComplianceRuleCreate, db: Session = Depends(get_db)):
    
    rule = ComplianceRule(**rule_data.dict())

    db.add(rule)
    db.commit()
    db.refresh(rule)

    return rule

@router.get("/",response_model=List[ComplianceRuleResponse])
def get_rule(db:Session = Depends(get_db)):
    rules = db.query(ComplianceRule).all()
    
    return rules
