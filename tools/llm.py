import os
import requests
from dotenv import load_dotenv

# 🔑 Force loading from current directory
load_dotenv(dotenv_path=".env", override=True)

OPENROUTER_API_KEY = os.getenv("OPENAI_API_KEY")
OPENROUTER_MODEL = os.getenv("OPENAI_MODEL", "openai/gpt-4.1")

OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"

if not OPENROUTER_API_KEY:
    raise RuntimeError("OPENAI_API_KEY is not loaded. Check .env file.")


def call_llm(system, user):
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://example.com",
        "X-Title": "Deep Research Assistant",
        "User-Agent": "DeepResearchAssistant/1.0"
    }

    payload = {
        "model": OPENROUTER_MODEL,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": user}
        ],
        "temperature": 0.3,
        "max_tokens": 800
    }

    response = requests.post(
        OPENROUTER_URL,
        headers=headers,
        json=payload,
        timeout=60
    )

    if response.status_code != 200:
        raise Exception(f"LLM Error {response.status_code}: {response.text}")

    return response.json()["choices"][0]["message"]["content"]
