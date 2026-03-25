"""Core chatbot orchestration."""

from __future__ import annotations

from pathlib import Path

from app.memory import ConversationMemory
from app.utils import format_knowledge_base, load_knowledge_base
from models.llm import LLMClient


class ChatBot:
    def __init__(
        self,
        llm_client: LLMClient,
        memory: ConversationMemory,
        knowledge_base_path: str | Path | None = None,
    ) -> None:
        self.llm_client = llm_client
        self.memory = memory
        self.knowledge_base_path = knowledge_base_path
        self.system_prompt = self._build_system_prompt()

    def _build_system_prompt(self) -> str:
        if not self.knowledge_base_path:
            return "You are a helpful AI chatbot."

        knowledge_base = load_knowledge_base(self.knowledge_base_path)
        context = format_knowledge_base(knowledge_base)
        return (
            "You are a helpful AI chatbot. Use the following custom knowledge when relevant:\n"
            f"{context}"
        )

    def reply(self, user_message: str) -> str:
        self.memory.add_message("user", user_message)
        messages = [{"role": "system", "content": self.system_prompt}, *self.memory.get_messages()]
        assistant_message = self.llm_client.generate_response(messages)
        self.memory.add_message("assistant", assistant_message)
        return assistant_message

