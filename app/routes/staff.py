from fastapi import APIRouter, HTTPException
from app.models.staff import Staff
from app.state import staff_db
from uuid import uuid4

router = APIRouter(
    prefix="/staff",
    tags=["Staff"]
)

@router.post("/", response_model=Staff, status_code=201)
def create_staff(staff: Staff):
    staff.id = str(uuid4())
    staff_db.append(staff)
    return staff

@router.get("/", response_model=list[Staff])
def get_all_staff():
    return staff_db

@router.get("/{staff_id}", response_model=Staff)
def get_staff_by_id(staff_id: str):
    for staff in staff_db:
        if staff.id == staff_id:
            return staff
    raise HTTPException(status_code=404, detail="Staff not found")

@router.put("/{staff_id}", response_model=Staff)
def update_staff(staff_id: str, updated_staff: Staff):
    for i, staff in enumerate(staff_db):
        if staff.id == staff_id:
            updated_staff.id = staff_id
            staff_db[i] = updated_staff
            return updated_staff
    raise HTTPException(status_code=404, detail="Staff not found")

@router.delete("/{staff_id}", status_code=204)
def delete_staff(staff_id: str):
    global staff_db
    staff_db = [staff for staff in staff_db if staff.id != staff_id]
    return
