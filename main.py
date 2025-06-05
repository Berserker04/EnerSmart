from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
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