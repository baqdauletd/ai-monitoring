from dataclasses import dataclass, field
from typing import Any, Literal

from tomlkit import datetime

# datatypes, event shapes, allowed event names
# for - starting/finishing, query generation, call API, normalization, deduplication, storing in psql

EventType = Literal["starting", "finishing", "query_generation", "call_api", "normalization", "deduplication", "storing_in_psql"]

@dataclass
class MonitoringEvent:
    run_id: str
    event_type: EventType
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat())
    payload: dict[str, Any]
    err: str | None = None