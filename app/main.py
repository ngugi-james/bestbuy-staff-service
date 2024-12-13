from fastapi import FastAPI
from app.routes import staff

app = FastAPI(
    title="Staff Service",
    description="A simple service to manage staff information.",
    version="1.0.0"
)

# Include routes
app.include_router(staff.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
