from fastapi import FastAPI
from routes.patient import router as PatientRouter
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Patient Dashboard API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(PatientRouter, prefix="/patients", tags=["Patients"])

@app.get("/")
async def root():
    return {"message": "Patient Dashboard API is running"}