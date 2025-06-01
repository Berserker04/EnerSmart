from src.model.diagnosticModel import DiagnosticRequest, Diagnostic
from src.model.recommendationModel import Recommendation
from src.store import recommendationStore, userStore

def perform_diagnostic(data: DiagnosticRequest) -> Diagnostic:
    all_recs: list[Recommendation] = recommendationStore.load_all()
    selected = [rec for rec in all_recs if rec.id in data.selected_ids]
    total_saving = sum(rec.estimated_saving for rec in selected)
    optimized_kwh = data.current_kwh * (1 - total_saving)

    diagnostic = Diagnostic(
        recommendations=[rec.description for rec in selected],
        optimized_kwh=optimized_kwh,
        total_saving_percent=total_saving * 100
    )
    
    userStore.add_diagnostic_to_user(data.user_id, diagnostic)

    return diagnostic
