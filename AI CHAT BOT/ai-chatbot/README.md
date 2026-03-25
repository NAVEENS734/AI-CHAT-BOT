# AI Chatbot

A simple AI chatbot starter project with:

- A lightweight Flask web UI
- A reusable chatbot core underneath the Flask app
- Config loading from `.env`
- In-memory conversation history
- Sample knowledge base data
- Basic unit tests

## Project Structure

```text
ai-chatbot/
├── app/
├── models/
├── routes/
├── static/
├── templates/
├── data/
├── tests/
├── .env
├── requirements.txt
├── README.md
└── run.py
```

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

Add your API key to `.env`:

```env
OPENAI_API_KEY=your_api_key_here
```

## Run The Flask App

```bash
python run.py
```

Then open `http://127.0.0.1:5000`.

## Alternative Flask Command

```bash
python -m routes.api
```

## Run Tests

```bash
pytest
```

## Notes

If no API key is set, the chatbot runs in demo mode and echoes the latest user message.
