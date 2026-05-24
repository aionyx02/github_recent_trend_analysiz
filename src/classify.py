"""Stage 4: rule-based, single-category classifier. See ADR-0004.

Priority order (first match wins):
    AI/ML > Security > DevOps > Data > Web > Mobile > Game > CLI/Tooling > Other

Match against lowercased description + topics + primary_language.
"""

from __future__ import annotations

import pandas as pd

CATEGORY_RULES: list[tuple[str, set[str]]] = [
    ("AI/ML", {
        "ai", "artificial-intelligence", "machine-learning", "ml", "deep-learning",
        "llm", "neural", "neural-network", "transformer", "diffusion", "agent",
        "agents", "rag", "embedding", "embeddings", "openai", "anthropic", "claude",
        "gpt", "fine-tuning", "pytorch", "tensorflow", "huggingface",
    }),
    ("Security", {
        "security", "vulnerability", "pentest", "pentesting", "malware",
        "exploit", "authentication", "encryption", "cryptography", "cve",
        "infosec", "appsec", "owasp",
    }),
    ("DevOps", {
        "docker", "kubernetes", "k8s", "ci", "cd", "ci-cd", "devops",
        "deployment", "terraform", "ansible", "helm", "argocd", "observability",
        "monitoring", "prometheus", "grafana", "infrastructure",
    }),
    ("Data", {
        "data", "database", "analytics", "visualization", "dashboard", "etl",
        "pandas", "spark", "sql", "warehouse", "lakehouse", "duckdb", "clickhouse",
    }),
    ("Web", {
        "react", "vue", "nextjs", "next-js", "svelte", "frontend", "backend",
        "web", "html", "css", "api", "nodejs", "node", "express", "fastapi",
        "django", "flask", "graphql", "rest", "tailwind",
    }),
    ("Mobile", {
        "android", "ios", "flutter", "react-native", "mobile", "swift",
        "kotlin", "objective-c",
    }),
    ("Game", {
        "game", "unity", "unreal", "godot", "graphics", "engine", "shader",
        "gamedev",
    }),
    ("CLI/Tooling", {
        "cli", "terminal", "command-line", "developer-tools", "productivity",
        "automation", "shell", "tui",
    }),
]

LANGUAGE_HINTS: dict[str, str] = {
    "swift": "Mobile",
    "kotlin": "Mobile",
    "objective-c": "Mobile",
    "dart": "Mobile",
    "glsl": "Game",
    "hlsl": "Game",
}


def _tokens(description: str, topics: list[str], primary_language: str) -> set[str]:
    text = description.lower()
    out = set(topics or [])
    for word in text.replace("/", " ").replace("-", " ").split():
        out.add(word.strip(".,;:!?()[]{}'\""))
    if primary_language:
        out.add(primary_language.lower())
    return out


def classify_one(description: str, topics: list[str], primary_language: str) -> str:
    tokens = _tokens(description, topics, primary_language)
    for category, keywords in CATEGORY_RULES:
        if tokens & keywords:
            return category
    if primary_language and primary_language.lower() in LANGUAGE_HINTS:
        return LANGUAGE_HINTS[primary_language.lower()]
    return "Other"


def apply(repos: pd.DataFrame, topics: pd.DataFrame) -> pd.DataFrame:
    """Return a copy of `repos` with a `category` column."""
    topics_by_repo = topics.groupby("repo_id")["topic"].apply(list).to_dict()
    out = repos.copy()
    out["category"] = [
        classify_one(
            row.description or "",
            topics_by_repo.get(row.id, []),
            row.primary_language or "",
        )
        for row in out.itertuples(index=False)
    ]
    return out