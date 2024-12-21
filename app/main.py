from fastapi import FastAPI, HTTPException, Depends
from pydantic import EmailStr
from database import db
from models import User
from utils import hash_password, verify_password

app = FastAPI()

@app.post("/register/")
async def register_user(user: User):
    """Register a new user."""
    if db.users.find_one({"email": user.email}):
        raise HTTPException(status_code=400, detail="Email already registered")
    user.password = hash_password(user.password)
    db.users.insert_one(user.dict(by_alias=True))
    return {"message": "User registered successfully"}

@app.post("/login/")
async def login(email: EmailStr, password: str):
    """Login an existing user."""
    user = db.users.find_one({"email": email})
    if not user or not verify_password(password, user["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"message": "Login successful"}

@app.post("/link-id/")
async def link_id(email: EmailStr, linked_id: str):
    """Link an external ID to the user."""
    user = db.users.find_one({"email": email})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    db.users.update_one({"email": email}, {"$set": {"linked_id": linked_id}})
    return {"message": "ID linked successfully"}

@app.get("/join/")
async def join_data():
    """Join data from another collection."""
    users = list(db.users.aggregate([
        {"$lookup": {
            "from": "another_collection",
            "localField": "_id",
            "foreignField": "user_id",
            "as": "joined_data"
        }}
    ]))
    return users

@app.delete("/delete-user/")
async def delete_user(email: EmailStr):
    """Delete a user and their related data."""
    user = db.users.find_one({"email": email})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    db.users.delete_one({"email": email})
    db.another_collection.delete_many({"user_id": user["_id"]})
    return {"message": "User and associated data deleted successfully"}
