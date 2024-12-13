from app.models.staff import Staff

# In-memory database for storing staff
staff_db: list[Staff] = [
    Staff(
        id="1",
        name="John Doe",
        position="Manager",
        department="Sales",
        email="john.doe@example.com",
        phone="123-456-7890"
    )
]
