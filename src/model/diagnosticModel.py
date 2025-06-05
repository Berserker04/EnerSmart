from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import date
import uuid

class DiagnosticRequest(BaseModel):
    selected_ids: List[int]
    current_kwh: float

class Diagnostic(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    recommendations: List[str]
    current_kwh: float
    optimized_kwh: float
    total_saving_percent: float
    create_date: date
