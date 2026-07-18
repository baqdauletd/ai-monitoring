import json

from monitoring.contract import MonitoringEvent


def event_to_dict(event: MonitoringEvent) -> dict:
    return {
        "run_id": event.run_id,
        "event_type": event.event_type,
        "timestamp": event.timestamp,
        "component": event.component,
        "operation": event.operation,
        "level": event.level,
        "duration_ms": event.duration_ms,
        "payload": event.payload,
        "error": event.error,
    }


def event_to_json(event: MonitoringEvent) -> str:
    return json.dumps(event_to_dict(event))


def log_event(event: MonitoringEvent) -> None:
    print(event_to_json(event))
