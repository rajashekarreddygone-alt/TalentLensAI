from .gemini_client import ask_gemini
from .prompts import INTERVIEW_PROMPT


def generate_interview_questions(resume_text):

    prompt = INTERVIEW_PROMPT.format(
        resume=resume_text
    )

    return ask_gemini(prompt)