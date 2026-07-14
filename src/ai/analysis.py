from http import client

from typer import prompt
from google.genai import types
from typer import prompt
from tenacity import retry, stop_after_attempt, wait_exponential

from src.ai import client
from src.ai.client import get_client
from src.ai.schemas import ResumeAnalysis


@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=2, max=10),
)
def analyze_resume_ai(resume_text: str, job_description: str):

    client = get_client()

    prompt = f"""
You are an expert AI Recruiter and ATS specialist.

Analyze the candidate's resume against the provided job description.

Return ONLY a JSON object matching the required schema.

-------------------------------------------------------
JOB DESCRIPTION
-------------------------------------------------------

{job_description}

-------------------------------------------------------
RESUME
-------------------------------------------------------

{resume_text}

-------------------------------------------------------
Your analysis should include:

1. Professional resume summary.

2. ATS feedback based on THIS job.

3. Explain why the ATS score is high or low.

4. Resume improvement suggestions specifically for THIS job.

5. Skill gap analysis.

6. AI career roadmap.

7. Generate interview questions based on BOTH:
   - Resume
   - Job Description

Interview questions should contain:

• Technical Questions
• Behavioral Questions
• HR Questions

Focus on identifying:

- Matching skills
- Missing skills
- Relevant experience
- Resume weaknesses
- Hiring recommendation
"""
    try:
        response = client.models.generate_content(
            model="gemini-3.1-flash-lite",
            contents=prompt,
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                response_schema=ResumeAnalysis,
            ),
        )

        return response.parsed

    except Exception:
        import traceback

        traceback.print_exc()
        raise