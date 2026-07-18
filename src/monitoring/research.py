from monitoring.contract import MonitoringEvent
from monitoring.logger import log_event


def query_generation_event(run_id: str, prompt: str, generated_queries: list[str], error: str | None = None,) -> MonitoringEvent:
    return MonitoringEvent(
        run_id=run_id,
        event_type="query_generation_successful" if error is None else "query_generation_failed",
        component="academic_research_agent",
        operation="query_generation",
        level="info" if error is None else "error",
        payload={
            "prompt": prompt,
            "queries": generated_queries,
            "query_count": len(generated_queries),
        },
        error=error,
    )


def log_query_generation(run_id: str, prompt: str, generated_queries: list[str], error: str | None = None,) -> None:
    log_event(query_generation_event(run_id, prompt, generated_queries, error))
