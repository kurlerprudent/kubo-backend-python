from fastapi import APIRouter, HTTPException
from models.patient import PatientModel, UpdatePatientModel
from schemas.patient import patient_helper
from database.mongodb import db
from bson import ObjectId

router = APIRouter()
collection = db["patients"]

@router.post("/", response_description="Add new patient")
async def add_patient(patient: PatientModel):
    #new_patient = await collection.insert_one(patient.dict())
   # created_patient = await collection.find_one({"_id": new_patient.inserted_id})
    return patient

@router.get("/", response_description="List all patients")
async def get_patients():
    patients = []
    async for patient in collection.find():
        patients.append(patient_helper(patient))
    return patients

@router.get("/{id}", response_description="Get a patient")
async def get_patient(id: str):
    patient = await collection.find_one({"_id": ObjectId(id)})
    if patient:
        return patient_helper(patient)
    raise HTTPException(status_code=404, detail="Patient not found")

@router.put("/{id}", response_description="Update a patient")
async def update_patient(id: str, data: UpdatePatientModel):
    update_data = {k: v for k, v in data.dict().items() if v is not None}
    if len(update_data) >= 1:
        result = await collection.update_one({"_id": ObjectId(id)}, {"$set": update_data})
        if result.modified_count == 1:
            updated = await collection.find_one({"_id": ObjectId(id)})
            return patient_helper(updated)
    raise HTTPException(status_code=404, detail="Patient not found")

@router.delete("/{id}", response_description="Delete a patient")
async def delete_patient(id: str):
    result = await collection.delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 1:
        return {"status": "Patient deleted successfully"}
    raise HTTPException(status_code=404, detail="Patient not found")