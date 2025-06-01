from fastapi import APIRouter, HTTPException
from src.model.authModel import AuthRequest
from src.model.userModel import User
from src.service import authService

router = APIRouter()

@router.post("/login", response_model=User)
def login(credentials: AuthRequest):
    try:
        return authService.authenticate(credentials.userName, credentials.password)
    except ValueError:
        raise HTTPException(status_code=401, detail="Usuario o contraseña incorrectos")
