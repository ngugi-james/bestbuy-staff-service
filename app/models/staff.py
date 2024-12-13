from pydantic import BaseModel

class Staff(BaseModel):
    id: str | None = None
    name: str
    position: str
    department: str
    email: str  # Changed from EmailStr to str for basic validation
    phone: str
