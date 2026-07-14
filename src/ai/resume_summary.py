from src.ai.client import ask_gemini
from src.ai.prompts import RESUME_SUMMARY_PROMPT


def generate_resume_summary(resume_text: str):

    prompt = RESUME_SUMMARY_PROMPT.format(
        resume=resume_text
    )

    # use the genai client to send the prompt
    response = ask_gemini(prompt)
    return response