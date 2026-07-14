from src.ai.gemini_client import ask_gemini
from src.ai.prompts import ATS_FEEDBACK_PROMPT


def generate_ats_feedback(resume_text: str):

    prompt = ATS_FEEDBACK_PROMPT.format(
        resume=resume_text
    )

    return ask_gemini(prompt)