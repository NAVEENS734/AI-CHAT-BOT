"""Conversation memory storage."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List


@dataclass
class ConversationMemory:
    max_messages: int = 10
    messages: List[Dict[str, str]] = field(default_factory=list)

    def add_message(self, role: str, content: str) -> None:
        self.messages.append({"role": role, "content": content})
        if len(self.messages) > self.max_messages:
            self.messages = self.messages[-self.max_messages :]

    def get_messages(self) -> List[Dict[str, str]]:
        return list(self.messages)

    def clear(self) -> None:
        self.messages.clear()

