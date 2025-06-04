from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
# from model.recommendationModel import CalculationRequest, RecommendationResponse
# from src.logic.logic import load_recommendations, filter_and_calculate
from src.controller.recommendationController import router as recommendation_router
from src.controller.userController import router as user_router
from src.controller.diagnosticController import router as diagnostic_router
from src.controller.authController import router as auth_router

app = FastAPI(title="EnerSmart")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

api_router = APIRouter(prefix="/api")
api_router.include_router(recommendation_router, prefix="/recommendations", tags=["Recommendations"])
api_router.include_router(user_router, prefix="/users", tags=["Users"])
api_router.include_router(diagnostic_router, prefix="/diagnostic", tags=["Diagnostic"])
api_router.include_router(auth_router, prefix="/auth", tags=["Auth"])

app.include_router(api_router)

# recommendations = load_recommendations()

# @app.post("/calculate", response_model=RecommendationResponse)
# def calculate_optimized_consumption(data: CalculationRequest):
#     selected, optimized_kwh, saving_percent = filter_and_calculate(
#         data.selected_ids,
#         data.current_kwh,
#         recommendations
#     )
#     return RecommendationResponse(
#         selected=selected,
#         optimized_kwh=optimized_kwh,
#         total_saving_percent=saving_percent
#     )
