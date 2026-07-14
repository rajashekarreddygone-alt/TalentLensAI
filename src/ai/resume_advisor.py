from src.ai.gemini_client import ask_gemini
from src.ai.prompts import RESUME_ADVISOR_PROMPT


def generate_resume_advice(resume_text: str):

    prompt = RESUME_ADVISOR_PROMPT.format(
        resume=resume_text
    )

    return ask_gemini(prompt)