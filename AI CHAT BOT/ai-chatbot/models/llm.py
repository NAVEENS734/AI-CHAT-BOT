"""LLM client wrapper with a local fallback mode."""

from __future__ import annotations

from typing import Dict, List


class LLMClient:
    def __init__(self, api_key: str, model_name: str, temperature: float = 0.7) -> None:
        self.api_key = api_key
        self.model_name = model_name
        self.temperature = temperature

    def generate_response(self, messages: List[Dict[str, str]]) -> str:
        user_message = next(
            (message["content"] for message in reversed(messages) if message["role"] == "user"),
            "",
        )

        if not self.api_key:
            return (
                "Demo mode: add your OPENAI_API_KEY to .env to enable real model responses. "
                f"You said: {user_message}"
            )

        try:
            from openai import OpenAI
        except ImportError:
            return "The OpenAI package is not installed. Run `pip install -r requirements.txt`."

        client = OpenAI(api_key=self.api_key)
        response = client.chat.completions.create(
            model=self.model_name,
            temperature=self.temperature,
            messages=messages,
        )
        return response.choices[0].message.content or "No response received."

