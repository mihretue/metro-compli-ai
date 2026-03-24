from app.models.compliance_rule import ComplianceRule
from app.models.emission_record import EmissionRecord


def calculate_compliance(db, building, year):
    # Get emission Record
    record = db.query(EmissionRecord).filter(
        EmissionRecord.building_id == building.id,
        EmissionRecord.year == year
    ).first()
    
    if not record:
        return None
    
    # Get Rule 
    rule = db.query(ComplianceRule).filter(
        ComplianceRule.year == year
    ).first()
    
    if not rule:
        return None
    
    
    actual = record.emissions or 0
    limit = rule.emission_limit 
    
    excess = max(0, actual - limit)
    fine = excess * rule.penalty_per_ton
    
    # Status Classification
    if excess == 0:
        status = "compliant"
    elif excess < 5:
        status = "at-risk"
    else:
        status = "non-compliant"
        
    return {
        "actual_emissions": actual,
        "allowed_limit": limit,
        "excess_emissions": excess,
        "estimated_fine": fine,
        "status": status
    }   
    