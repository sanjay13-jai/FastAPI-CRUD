from fastapi import APIRouter, HTTPException
from models.user import User
# from utils.file_handler import load_users, save_users
from services.user_service import *

router = APIRouter()

# users = load_users()

#create user
@router.post("/create-user")
def create_user(user: User):
    try:
        user.id = generate_user_id()
        return create_user_service(user)
    except ValueError as e: 
        HTTPException(status_code=400, detail=str(e))


#get all users
@router.get("/all-users")
def get_users():
    return get_all_users_service()

#get single user
@router.post("/get-user/{user_id}")
def get_user(user_id: int):
    user = get_user_service(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

#Update user
@router.put("/update_user/{user_id}")
def update_user(user_id: int, updated_user: User):
    user = update_user_service(user_id, updated_user)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user       

#Delete User
@router.delete("/delete-user/{user_id}")
def delete_user(user_id: int):
    success = delete_user_service(user_id)
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted"}        