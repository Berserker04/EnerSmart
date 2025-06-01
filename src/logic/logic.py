import json
from src.model.models import Recommendation


def load_recommendations(path="src/db/recommendations.json") -> list[Recommendation]:
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return [Recommendation(**item) for item in data]


def filter_and_calculate(selected_ids: list[int], current_kwh: float, all_recs: list[Recommendation]):
    selected = [rec for rec in all_recs if rec.id in selected_ids]
    total_saving = sum([rec.estimated_saving for rec in selected])
    optimized_kwh = current_kwh * (1 - total_saving)
    return selected, optimized_kwh, total_saving * 100  # porcentaje