from fastapi import APIRouter, HTTPException
from typing import List
from src.model.userModel import User
from src.service import userService

router = APIRouter()

@router.get("/", response_model=List[User])
def get_users():
    return userService.get_all_users()

@router.get("/{id}", response_model=User)
def get_user(id: int):
    try:
        return userService.get_user_by_id(id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.post("/", response_model=User)
def create_user(user: User):
    userService.add_user(user)
    return user

@router.put("/", response_model=User)
def update_user(user: User):
    try:
        userService.update_user(user)
        return user
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/{id}")
def delete_user(id: int):
    userService.delete_user(id)
    return {"message": f"User {id} deleted"}
