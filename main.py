from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.model.models import CalculationRequest, RecommendationResponse
from src.logic.logic import load_recommendations, filter_and_calculate

app = FastAPI(title="EnerSmart")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

recommendations = load_recommendations()

@app.post("/calculate", response_model=RecommendationResponse)
def calculate_optimized_consumption(data: CalculationRequest):
    selected, optimized_kwh, saving_percent = filter_and_calculate(
        data.selected_ids,
        data.current_kwh,
        recommendations
    )
    return RecommendationResponse(
        selected=selected,
        optimized_kwh=optimized_kwh,
        total_saving_percent=saving_percent
    )
