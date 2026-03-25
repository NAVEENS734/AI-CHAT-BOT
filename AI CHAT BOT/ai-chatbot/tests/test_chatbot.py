from app.chatbot import ChatBot
from app.memory import ConversationMemory


class DummyLLMClient:
    def generate_response(self, messages):
        return f"Echo: {messages[-1]['content']}"


def test_chatbot_reply_uses_latest_user_message():
    chatbot = ChatBot(
        llm_client=DummyLLMClient(),
        memory=ConversationMemory(max_messages=6),
    )

    reply = chatbot.reply("Hello")

    assert reply == "Echo: Hello"


def test_memory_trims_old_messages():
    memory = ConversationMemory(max_messages=2)
    memory.add_message("user", "one")
    memory.add_message("assistant", "two")
    memory.add_message("user", "three")

    assert memory.get_messages() == [
        {"role": "assistant", "content": "two"},
        {"role": "user", "content": "three"},
    ]

