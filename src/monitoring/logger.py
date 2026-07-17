import json

from monitoring.contract import EventType, MonitoringEvent

def log_event(event: MonitoringEvent) -> None:
    print(json.dumps(
        {
            "run_id": event.run_id,
            "event_type": event.event_type,
            "timestamp": event.timestamp,
            "payload": event.payload,
            "error": event.err
        }
    ))
    
def log_query_generation(prompt: str, generated_queries: list, err: str | None = None) -> None:
    log_event(
        MonitoringEvent(
            event_type=EventType("query_generation"),
            payload={
                "prompt": prompt,
                "queries": generated_queries,
            },
            error=err
        )
    )