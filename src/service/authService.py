from src.model.userModel import User
from src.store.userStore import find_by_credentials

def authenticate(userName: str, password: str) -> User:
    user = find_by_credentials(userName, password)
    return user
