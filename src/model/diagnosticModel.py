from pydantic import BaseModel
from typing import List

class DiagnosticRequest(BaseModel):
    selected_ids: List[int]
    current_kwh: float

class Diagnostic(BaseModel):
    recommendations: List[str]
    optimized_kwh: float
    total_saving_percent: float
