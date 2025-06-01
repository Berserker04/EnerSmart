from src.model.userModel import User
from src.store import userStore

def get_all_users():
    return userStore.load_all()

def get_user_by_id(user_id: int):
    return userStore.get_user_by_id(user_id)

def add_user(user: User):
    userStore.add(user)

def update_user(user: User):
    userStore.update(user)

def delete_user(id: int):
    userStore.delete_by_id(id)
