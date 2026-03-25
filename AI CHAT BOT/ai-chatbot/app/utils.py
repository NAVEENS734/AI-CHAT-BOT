"""Utility helpers for the chatbot."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict


def load_knowledge_base(path: str | Path) -> Dict[str, Any]:
    file_path = Path(path)
    if not file_path.exists():
        return {"topics": []}
    with file_path.open("r", encoding="utf-8") as file:
        return json.load(file)


def format_knowledge_base(knowledge_base: Dict[str, Any]) -> str:
    topics = knowledge_base.get("topics", [])
    if not topics:
        return "No custom knowledge base loaded."

    lines = []
    for topic in topics:
        title = topic.get("title", "Untitled")
        content = topic.get("content", "")
        lines.append(f"- {title}: {content}")
    return "\n".join(lines)

