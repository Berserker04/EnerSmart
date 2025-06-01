from pydantic import BaseModel

class AuthRequest(BaseModel):
    userName: str
    password: str
