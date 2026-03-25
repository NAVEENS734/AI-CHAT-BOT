const chatBox = document.getElementById("chat-box");
const messageInput = document.getElementById("message-input");
const sendButton = document.getElementById("send-button");

function appendMessage(text, sender) {
  const message = document.createElement("div");
  message.className = `message ${sender}`;
  message.textContent = text;
  chatBox.appendChild(message);
  chatBox.scrollTop = chatBox.scrollHeight;
}

async function sendMessage() {
  const message = messageInput.value.trim();
  if (!message) {
    return;
  }

  appendMessage(message, "user");
  messageInput.value = "";
  sendButton.disabled = true;

  try {
    const response = await fetch("/api/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message }),
    });

    const data = await response.json();
    appendMessage(data.response || data.error || "No response received.", "bot");
  } catch (error) {
    appendMessage("Unable to reach the server. Please try again.", "bot");
  } finally {
    sendButton.disabled = false;
    messageInput.focus();
  }
}

sendButton.addEventListener("click", sendMessage);
messageInput.addEventListener("keydown", (event) => {
  if (event.key === "Enter") {
    sendMessage();
  }
});

appendMessage("Hello. Ask me anything to begin.", "bot");

