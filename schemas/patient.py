def patient_helper(patient) -> dict:
    return {
        "id": str(patient["_id"]),
        "name": patient["name"],
        "age": patient["age"],
        "gender": patient["gender"],
        "condition": patient.get("condition", ""),
        "image_url": patient.get("image_url", "")
    }