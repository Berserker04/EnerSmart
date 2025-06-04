from typing import List, Optional
from pydantic import BaseModel
from src.model.diagnosticModel import Diagnostic

class User(BaseModel):
    id: Optional[int] = None
    fullName: str
    userName: str
    password: str
    rol: Optional[str] = "Client"
    diagnostics: List[Diagnostic] = []
