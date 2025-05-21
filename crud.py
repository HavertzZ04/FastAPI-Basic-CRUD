from db import fake_db
from schemas import UserCreate, User
from typing import Optional


def get_all_users() -> list[dict]:
    return fake_db.get("users", [])


def get_user(id: int) -> Optional[dict]:
    for user in fake_db.get("users", []):
        if user["id"] == id:
            return user
    return None


def create_user(user: UserCreate) -> Optional[dict]:
    username = user.username.lower()
    for existing_user in fake_db.get("users", []):
        if existing_user["username"].lower() == username:
            return None  

    new_id = max([u["id"] for u in fake_db["users"]], default=0) + 1
    user_dict = user.model_dump()
    user_dict["id"] = new_id
    user_dict["username"] = username 

    fake_db["users"].append(user_dict)
    return user_dict


def edit_user(user: User) -> Optional[dict]:
    for index, existing_user in enumerate(fake_db.get("users", [])):
        if existing_user["id"] == user.id:
            updated_user = user.model_dump()
            updated_user["id"] = user.id
            updated_user["username"] = updated_user["username"].lower()
            fake_db["users"][index] = updated_user
            return updated_user
    return None


def delete_user(id: int) -> dict:
    for index, user in enumerate(fake_db.get("users", [])):
        if user["id"] == id:
            del fake_db["users"][index]
            return {"message": "User deleted successfully."}
    return None
