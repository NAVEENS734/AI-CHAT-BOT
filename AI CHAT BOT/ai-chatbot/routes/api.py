"""Simple Flask web API for the chatbot."""

from __future__ import annotations

from flask import Flask, jsonify, render_template, request

from app.main import build_chatbot


app = Flask(__name__, template_folder="../templates", static_folder="../static")
chatbot = build_chatbot()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/chat", methods=["POST"])
def chat():
    payload = request.get_json(silent=True) or {}
    message = str(payload.get("message", "")).strip()

    if not message:
        return jsonify({"error": "Message is required."}), 400

    response = chatbot.reply(message)
    return jsonify({"response": response})


if __name__ == "__main__":
    app.run(debug=True)

