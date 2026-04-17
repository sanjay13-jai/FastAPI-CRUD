from models.user import User
from utils.file_handler import load_users, save_users
from utils.logger import logger

users = load_users() #Act as a temp DB -> User Table

def create_user_service(new_user: User):
    for user in users:
        if user.id == new_user.id: #Checking the user is already exists
            raise ValueError("User with this ID aldready exists")
        
    users.append(new_user) #Adding the new user to the User Table
    save_users(users) #Save the User Table

    logger.info(f"User created: {new_user.name}")    

    return new_user #Returing New User


def generate_user_id():
    if not users: #If no users in User Table while creating new user, which is the first user
        return 1
    
    return max(user.id for user in users) + 1 #if already user in User Table add one more each time


def get_all_users_service():
    return users #returing all users from the User Table


def get_user_service(user_id: int):
    for user in users:
        if user.id == user_id: #Searching the requested user id in User table
            return user
    return None


def update_user_service(user_id: int, updated_user: User):
    for i, user in enumerate(users):
        if user.id == user_id: #
            users[i] = updated_user
            updated_user.id = user_id
            save_users(users)

            logger.info(f"User updated: {user_id}")

            return updated_user
        

def delete_user_service(user_id: int):
    for i, user in enumerate(users):
        if user.id == user_id:
            users.pop(i)
            save_users(users)

            logger.info(f"User deleted: {user_id}")

            return True
    return False    



