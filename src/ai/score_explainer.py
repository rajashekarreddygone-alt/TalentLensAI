from src.ai.gemini_client import ask_gemini
from src.ai.prompts import SCORE_EXPLANATION_PROMPT


def explain_score(score, strengths, weaknesses):

    prompt = SCORE_EXPLANATION_PROMPT.format(
        score=score,
        strengths=", ".join(strengths),
        weaknesses=", ".join(weaknesses),
    )

    return ask_gemini(prompt)