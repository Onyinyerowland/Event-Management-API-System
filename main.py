from fastapi import FastAPI
from routes import user, event, speaker, registration


app = FastAPI(title="Event Management API System")


app.include_router(user.router)
app.include_router(event.router)
app.include_router(speaker.router)
app.include_router(registration.router)

@app.get("/")
def read_root():
    return {"message":"Welcome to Event Mangement API"}
