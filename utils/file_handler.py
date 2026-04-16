import json
from models.user import User
FILE_PATH = "data/users.json"

def load_users():
    try:
        with open(FILE_PATH, 'r') as f:
            data = json.load(f)
            return [User(**user) for user in data]
    except:
        return []      

def save_users(users):
    with open(FILE_PATH, "w") as f:
        json.dump([user.dict() for user in users], f, indent=4)       
            