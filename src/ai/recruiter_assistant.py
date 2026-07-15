from src.ai.client import get_client


MODEL_NAME = "gemini-3.1-flash-lite"


def ask_recruiter_assistant(question, candidate_context):
    """
    Ask Gemini a recruiter-related question using only the
    analyzed candidate information provided by the application.
    """

    if not question or not question.strip():
        return "Please enter a question."

    if not candidate_context:
        return "No candidate data is available for analysis."

    client = get_client()

    prompt = f"""
You are an AI Recruiter Assistant inside an AI-powered recruitment platform.

Your job is to help a recruiter understand and compare analyzed candidates.

IMPORTANT RULES:
1. Use ONLY the candidate information provided below.
2. Do not invent candidate skills, experience, education, scores, or qualifications.
3. If the available candidate data is insufficient to answer a question, clearly say so.
4. Explain recommendations using evidence from the candidate data.
5. When comparing candidates, mention relevant strengths, weaknesses, scores, and recruiter status where available.
6. Do not make hiring decisions based on protected or sensitive personal characteristics.
7. Keep your answer clear, professional, and useful to a recruiter.
8. Treat recruiter notes as additional context, not as verified objective facts.

CANDIDATE DATA:
{candidate_context}

RECRUITER QUESTION:
{question}

Provide a concise but helpful answer based only on the candidate data above.
"""

    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt
        )

        if response and response.text:
            return response.text.strip()

        return "The AI assistant did not return a response."

    except Exception as error:
        return f"AI Recruiter Assistant error: {str(error)}"