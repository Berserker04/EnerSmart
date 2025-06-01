from pydantic import BaseModel
from typing import List


class Recommendation(BaseModel):
    id: int
    question: str
    description: str
    estimated_saving: float


class RecommendationResponse(BaseModel):
    selected: List[Recommendation]
    optimized_kwh: float
    total_saving_percent: float


class CalculationRequest(BaseModel):
    selected_ids: List[int]
    current_kwh: float
