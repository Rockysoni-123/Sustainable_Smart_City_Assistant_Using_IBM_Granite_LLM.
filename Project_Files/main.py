from fastapi import FastAPI

# Import routers
from chat_router import router as chat_router
from policy_router import router as policy_router
from eco_tips_router import router as eco_tips_router
from feedback_router import router as feedback_router
from report_router import router as report_router
from vector_router import router as vector_router
from kpi_upload_router import router as kpi_upload_router
from dashboard_router import router as dashboard_router

app = FastAPI(title="Sustainable Smart City Assistant")

# Include routers
app.include_router(chat_router)
app.include_router(policy_router)
app.include_router(eco_tips_router)
app.include_router(feedback_router)
app.include_router(report_router)
app.include_router(vector_router)
app.include_router(kpi_upload_router)
app.include_router(dashboard_router)

# Optional root route
@app.get("/")
async def root():
    return {"message": "Welcome to the Sustainable Smart City API!"}
