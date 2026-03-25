"""CLI entry point for the chatbot."""

from __future__ import annotations

from pathlib import Path

from app.chatbot import ChatBot
from app.config import BASE_DIR, get_settings
from app.memory import ConversationMemory
from models.llm import LLMClient


def build_chatbot() -> ChatBot:
    settings = get_settings()
    llm_client = LLMClient(
        api_key=settings.openai_api_key,
        model_name=settings.model_name,
        temperature=settings.temperature,
    )
    memory = ConversationMemory(max_messages=settings.max_history)
    knowledge_base_path = Path(BASE_DIR) / "data" / "knowledge_base.json"
    return ChatBot(llm_client=llm_client, memory=memory, knowledge_base_path=knowledge_base_path)


def run_cli() -> None:
    chatbot = build_chatbot()
    print("AI Chatbot is ready. Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in {"exit", "quit"}:
            print("Bot: Goodbye!")
            break
        if not user_input:
            print("Bot: Please enter a message.")
            continue
        print(f"Bot: {chatbot.reply(user_input)}\n")


if __name__ == "__main__":
    run_cli()

