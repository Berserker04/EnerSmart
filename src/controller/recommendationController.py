from fastapi import APIRouter, HTTPException
from typing import List
from src.model.recommendationModel import Recommendation
from src.service import recommendationService

router = APIRouter()

@router.get("/", response_model=List[Recommendation])
def get_recommendations():
    return recommendationService.get_all_recommendations()

@router.post("/", response_model=Recommendation)
def create_recommendation(rec: Recommendation):
    recommendationService.add_recommendation(rec)
    return rec

@router.put("/", response_model=Recommendation)
def update_recommendation(rec: Recommendation):
    try:
        recommendationService.update_recommendation(rec)
        return rec
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/{id}")
def delete_recommendation(id: int):
    recommendationService.delete_recommendation(id)
    return {"message": f"Recommendation {id} deleted"}
