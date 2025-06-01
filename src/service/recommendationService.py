from src.model.recommendationModel import Recommendation
from src.store import recommendationStore

def get_all_recommendations():
    return recommendationStore.load_all()

def add_recommendation(rec: Recommendation):
    recommendationStore.add(rec)

def update_recommendation(rec: Recommendation):
    recommendationStore.update(rec)

def delete_recommendation(id: int):
    recommendationStore.delete_by_id(id)
