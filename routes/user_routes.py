from fastapi import APIRouter, HTTPException
from models.user import User
from utils.file_handler import load_users, save_users

router = APIRouter()

users = load_users()

#create user
@router.post("/create-user")
def create_user(user: User):
    users.append(user)
    save_users(users)
    return {"message": "User created"}

#get all users
@router.get("/all-users")
def get_users():
    return users    

#get single user
@router.post("/get-user/{user_id}")
def get_user(user_id: int):
    for user in users:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")   

#Update user
@router.put("/update_user/{user_id}")
def update_user(user_id: int, updated_user: User):
    for i, user in enumerate(users):
        if user.id == user_id:
            users[i] = updated_user
            save_users(users)    
            return {"message": "User updated"}
    raise HTTPException(status_code=404, detail="User not found")        

#Delete User
@router.delete("/delete-user/{user_id}")
def delete_user(user_id: int):
    for i, user in enumerate(users):
        if user.id == user_id:
            users.pop(i)
            save_users(users)
            return {"message": "User deleted"}
    raise HTTPException(status_code=404, detail="User not found")        