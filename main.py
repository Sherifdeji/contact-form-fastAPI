from fastapi import FastAPI
from pydantic import BaseModel, EmailStr, Field

app = FastAPI(title="Contact Form API")

class ContactMessage(BaseModel):
    name: str
    email: EmailStr
    message: str = Field(..., min_length=10, description="Message must be at least 10 characters long")
    subject: str = "General Inquiry"

@app.get("/")
async def root():
    return {"message": "Welcome to the Contact Form API!"}

@app.post("/contact")
async def submit_contact_form(contact: ContactMessage):
    return{
         "status": "success",
        "info": f"Message received from {contact.name}.",
    }