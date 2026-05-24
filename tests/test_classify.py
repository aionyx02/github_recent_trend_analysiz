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