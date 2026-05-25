"""Unit tests for src.classify — rule-based, deterministic."""

import pytest

from src.classify import classify_one

PRIORITY_CASES = [
    ("LLM agent platform", ["llm", "agent"], "Python", "AI/ML"),
    ("pentest framework", ["security"], "Rust", "Security"),
    ("k8s helm operator", ["kubernetes"], "Go", "DevOps"),
    ("interactive analytics dashboard", ["dashboard"], "TypeScript", "Data"),
    ("nextjs starter", ["react", "nextjs"], "TypeScript", "Web"),
    ("flutter app", ["flutter"], "Dart", "Mobile"),
    ("godot game engine", ["godot"], "C++", "Game"),
    ("fancy terminal multiplexer", ["cli", "terminal"], "Rust", "CLI/Tooling"),
    ("some random thing", [], "", "Other"),
]


@pytest.mark.parametrize("desc,topics,lang,expected", PRIORITY_CASES)
def test_classify_one(desc, topics, lang, expected):
    assert classify_one(desc, topics, lang) == expected


def test_ai_ml_beats_web_when_both_match():
    """Priority order: AI/ML > Web. A 'react LLM agent' goes to AI/ML."""
    assert classify_one("react frontend for llm agent", ["react", "llm"], "TypeScript") == "AI/ML"


def test_data_beats_web():
    """Per ADR-0004 priority order, Data outranks Web."""
    assert classify_one("react dashboard", ["react"], "TypeScript") == "Data"


def test_language_hint_falls_back_when_no_keyword():
    """Pure Swift project with no description/topics should land in Mobile."""
    assert classify_one("", [], "Swift") == "Mobile"


def test_description_is_tokenized_case_insensitive():
    assert classify_one("Docker-based CI helper", [], "Shell") == "DevOps"


def test_classify_finance_trading_polymarket():
    """Polymarket arbitrage bot should land in Finance/Trading, not Other."""
    assert classify_one(
        "Polymarket arbitrage trading bot",
        ["polymarket", "arbitrage-bot"],
        "Python",
    ) == "Finance/Trading"


def test_classify_ai_ml_claude_code_topic():
    """A repo whose only AI/ML signal is the `claude-code` topic must still hit AI/ML."""
    assert classify_one(
        "Workflow recipes for shipping with the editor",
        ["claude-code"],
        "TypeScript",
    ) == "AI/ML"


def test_classify_priority_ai_beats_finance():
    """AI/ML outranks Finance/Trading: an LLM-driven trading agent stays AI/ML."""
    assert classify_one(
        "LLM agent that trades on polymarket",
        ["llm", "trading"],
        "Python",
    ) == "AI/ML"