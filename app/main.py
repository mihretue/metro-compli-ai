from fastapi import FastAPI
from app.core.config import settings
from app.db.base import Base
from app.db.session import engine
from app.models import *
from app.api.routes import upload
from app.api.routes import rule
from app.api.routes import compliance

app = FastAPI(title=settings.APP_NAME)
Base.metadata.create_all(bind=engine)

app.include_router(upload.router, prefix="/api")
app.include_router(rule.router, prefix="/api")
app.include_router(compliance.router, prefix="/api")

@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "app": settings.APP_NAME
    }
    
