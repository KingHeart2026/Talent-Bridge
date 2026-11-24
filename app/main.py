from fastapi import FastAPI
from app.routes import auth
from app.routes import candidates
from app.routes import companies
from app.routes import admin


app = FastAPI(
    title="KING HEART TalentBridge API",
    description="Job Board and Applicant Tracking API",
    version="1.0.0"
)


# Register authentication routes
app.include_router(auth.router, prefix="/api/v1")

# Register candidate routes
app.include_router(candidates.router, prefix="/api/v1")

# Register company routes
app.include_router(companies.router, prefix="/api/v1")

# Register admin routes
app.include_router(admin.router, prefix="/api/v1")


@app.get("/health", tags=["General"])
def health_check():
    return {
        "status": "healthy",
        "application": "TalentBridge API"
    }