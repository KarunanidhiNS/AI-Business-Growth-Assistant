import requests
from config import Config

API_URL = "https://api.mistral.ai/v1/chat/completions"

def ask_mistral(prompt):

    try:

        headers = {
            "Authorization":
            f"Bearer {Config.MISTRAL_API_KEY}",
            "Content-Type":
            "application/json"
        }

        payload = {
            "model":
            "mistral-small-latest",

            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        }

        response = requests.post(
            API_URL,
            json=payload,
            headers=headers,
            timeout=30
        )

        response.raise_for_status()

        return (
            response.json()
            ["choices"][0]
            ["message"]
            ["content"]
        )

    except Exception as e:

        return f"AI Analysis Error: {str(e)}"