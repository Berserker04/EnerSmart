from fastapi import APIRouter, HTTPException
from src.model.diagnosticModel import DiagnosticRequest, Diagnostic
from src.service import diagnosticService

router = APIRouter()

@router.post("/{id}", response_model=Diagnostic)
def run_diagnostic(id: int, data: DiagnosticRequest):
    try:
        return diagnosticService.perform_diagnostic(id, data)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
