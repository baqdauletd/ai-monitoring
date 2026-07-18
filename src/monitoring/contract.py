from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Literal

EventLevel = Literal["debug", "info", "warning", "error"]

@dataclass
class MonitoringEvent:
    run_id: str
    event_type: str
    payload: dict[str, Any] = field(default_factory=dict)
    timestamp: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    component: str | None = None
    operation: str | None = None
    level: EventLevel = "info"
    duration_ms: float | None = None
    error: str | None = None
