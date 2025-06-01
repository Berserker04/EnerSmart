import json
from typing import List
from src.model.recommendationModel import Recommendation

path = "src/db/recommendations.json"

def load_all() -> List[Recommendation]:
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return [Recommendation(**item) for item in data]

def save_all(recommendations: List[Recommendation]):
    with open(path, "w", encoding="utf-8") as f:
        json.dump([r.model_dump() for r in recommendations], f, ensure_ascii=False, indent=2)

def add(recommendation: Recommendation):
    recs = load_all()
    recommendation.id = max((u.id for u in recs), default=0) + 1
    recs.append(recommendation)
    save_all(recs)

def delete_by_id(id: int):
    recs = load_all()
    recs = [r for r in recs if r.id != id]
    save_all(recs)

def update(recommendation: Recommendation):
    recs = load_all()
    updated = False
    for i, r in enumerate(recs):
        if r.id == recommendation.id:
            recs[i] = recommendation
            updated = True
            break
    if not updated:
        raise ValueError(f"No recommendation with id {recommendation.id}")
    save_all(recs)
