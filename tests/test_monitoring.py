import json
from datetime import datetime

from monitoring import MonitoringEvent, event_to_dict, event_to_json, log_event
from monitoring.research import log_query_generation, query_generation_event


def test_monitoring_event_defaults():
    event = MonitoringEvent(run_id="run-1", event_type="test_event")

    assert event.run_id == "run-1"
    assert event.event_type == "test_event"
    assert event.payload == {}
    assert event.level == "info"
    assert event.error is None
    assert datetime.fromisoformat(event.timestamp)


def test_event_to_dict_contains_generic_fields():
    event = MonitoringEvent(
        run_id="run-1",
        event_type="source_failed",
        component="agent",
        operation="search",
        level="error",
        duration_ms=12.5,
        payload={"source": "openalex"},
        error="timeout",
    )

    data = event_to_dict(event)

    assert data == {
        "run_id": "run-1",
        "event_type": "source_failed",
        "timestamp": event.timestamp,
        "component": "agent",
        "operation": "search",
        "level": "error",
        "duration_ms": 12.5,
        "payload": {"source": "openalex"},
        "error": "timeout",
    }


def test_event_to_json_outputs_valid_json():
    event = MonitoringEvent(
        run_id="run-1",
        event_type="papers_stored",
        payload={"stored_count": 10},
    )

    data = json.loads(event_to_json(event))

    assert data["run_id"] == "run-1"
    assert data["event_type"] == "papers_stored"
    assert data["payload"] == {"stored_count": 10}


def test_log_event_prints_json(capsys):
    event = MonitoringEvent(run_id="run-1", event_type="run_started")

    log_event(event)

    data = json.loads(capsys.readouterr().out)
    assert data["run_id"] == "run-1"
    assert data["event_type"] == "run_started"


def test_query_generation_event_success():
    event = query_generation_event(
        run_id="run-1",
        prompt="iot lora",
        generated_queries=["iot lora papers", "2.4 ghz lora research"],
    )

    assert event.event_type == "query_generation_successful"
    assert event.component == "academic_research_agent"
    assert event.operation == "query_generation"
    assert event.level == "info"
    assert event.payload["query_count"] == 2


def test_query_generation_event_failure():
    event = query_generation_event(
        run_id="run-1",
        prompt="iot lora",
        generated_queries=[],
        error="model failed",
    )

    assert event.event_type == "query_generation_failed"
    assert event.level == "error"
    assert event.error == "model failed"


def test_log_query_generation_prints_research_event(capsys):
    log_query_generation("run-1", "iot lora", ["iot lora papers"])

    data = json.loads(capsys.readouterr().out)
    assert data["event_type"] == "query_generation_successful"
    assert data["component"] == "academic_research_agent"
    assert data["payload"]["query_count"] == 1
