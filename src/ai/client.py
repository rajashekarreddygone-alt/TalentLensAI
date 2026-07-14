import os
from google import genai

_client = None

def get_client():
    global _client

    if _client is None:
        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise ValueError(
                "GEMINI_API_KEY environment variable is not set."
            )

        _client = genai.Client(api_key=api_key)

    return _client