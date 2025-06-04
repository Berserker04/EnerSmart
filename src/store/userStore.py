import json
from typing import List
from src.model.userModel import User
from src.model.diagnosticModel import Diagnostic

path = "src/db/users.json"

def load_all() -> List[User]:
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return [User(**item) for item in data]

def get_user_by_id(user_id: int) -> User:
    users = load_all()
    for u in users:
        if u.id == user_id:
            return u
    raise ValueError(f"No user found with id {user_id}")


def save_all(users: List[User]):
    with open(path, "w", encoding="utf-8") as f:
        json.dump([u.model_dump(mode="json") for u in users], f, ensure_ascii=False, indent=2)

def add(user: User):
    users = load_all()
    user.id = max((u.id for u in users), default=0) + 1
    users.append(user)
    save_all(users)

def delete_by_id(id: int):
    users = load_all()
    users = [u for u in users if u.id != id]
    save_all(users)

def update(user: User):
    users = load_all()
    updated = False
    for i, u in enumerate(users):
        if u.id == user.id:
            users[i] = user
            updated = True
            break
    if not updated:
        raise ValueError(f"No user with id {user.id}")
    save_all(users)

def add_diagnostic_to_user(user_id: int, diagnostic: Diagnostic):
    users = load_all()
    found = False
    for u in users:
        if u.id == user_id:
            u.diagnostics.append(diagnostic)
            found = True
            break
    if not found:
        raise ValueError(f"No user with id {user_id}")
    save_all(users)

def find_by_credentials(username: str, password: str) -> User:
    users = load_all()
    for u in users:
        if u.userName == username and u.password == password:
            u.diagnostics = u.diagnostics[::-1]
            return u
    raise ValueError("Credenciales inválidas")
