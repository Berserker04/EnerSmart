from pydantic import BaseModel
from typing import List, Optional


class Recommendation(BaseModel):
    id: Optional[int] = None
    question: str
    description: str
    estimated_saving: float


# class RecommendationResponse(BaseModel):
#     selected: List[Recommendation]
#     optimized_kwh: float
#     total_saving_percent: float


