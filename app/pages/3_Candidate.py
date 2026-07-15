import streamlit as st

from app.components.job_match import display_job_match
from src.matching.job_matcher import calculate_job_match
from app.components.ai_summary import show_ai_summary
from app.components.ats_card import show_ats_card
from app.components.interview_questions import show_interview_questions
from app.components.resume_advisor import show_resume_advice
from src.parser.resume_parser import parse_resume
from src.ai.analysis import analyze_resume_ai
from src.parser.job_parser import parse_job_description
from app.components.should_apply import show_should_apply
from app.components.skill_gap import show_skill_gap
from app.components.career_roadmap import show_career_roadmap
from app.components.pdf_generator import generate_pdf



st.title("🎓 Candidate Dashboard")

resume_file = st.file_uploader(
    "Upload Your Resume",
    type=["pdf", "docx"]
)

if resume_file:
   import tempfile
   import os

   from src.parser.resume_parser import parse_resume
   from src.ai.analysis import analyze_resume_ai


   st.success("Resume uploaded successfully!")

 # -------------------------------------------------
 # Save uploaded file temporarily
 # -------------------------------------------------

   suffix = os.path.splitext(resume_file.name)[1]

   with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:

    tmp.write(resume_file.getbuffer())

    temp_path = tmp.name

 # -------------------------------------------------
 # Parse Resume
 # -------------------------------------------------

   resume = parse_resume(temp_path)

 # Remove temporary file

   os.remove(temp_path)

   # Derive candidate name from uploaded file or fallback
   candidate_name = os.path.splitext(resume_file.name)[0] if resume_file else "Candidate"

 
   # ==========================================================
# Job Description Matching
# ==========================================================

st.divider()

st.header("💼 Job Match Analysis")

job_description = st.text_area(
    "Paste the Job Description",
    height=250,
    placeholder="""
Example:

Machine Learning Engineer

Requirements:

- Python
- TensorFlow
- SQL
- Docker
- AWS
- Machine Learning
"""
)

if job_description.strip():

  job_data = parse_job_description(job_description)
  
  match = calculate_job_match(
    resume,
    type(
      "Job",
      (),
      {
        "text": job_data["text"],
        "skills": job_data["skills"],
      },
    )(),
  )
  display_job_match(match)
  st.info(
    "The Job Compatibility Score measures how well your resume aligns with "
    "the selected job description based on factors such as skills, semantic "
    "similarity, experience, education, and keyword coverage. "
    "This score may differ from the Recruiter Ranking Score, which considers "
    "additional candidate evaluation factors."
   )
  show_should_apply(match)

  st.divider()

  st.header("🤖 AI Analysis")

  with st.spinner("AI is analyzing your resume against the job description..."):

        analysis = analyze_resume_ai(
            resume.raw_text,
            job_description
        )
  show_career_roadmap(analysis)
  show_ai_summary(analysis)
  show_ats_card(analysis)
  show_resume_advice(analysis)
  show_interview_questions(analysis)

  report_data = {
    "candidate_name": candidate_name,
    "overall_match": match.overall_match,
    "skill_match": getattr(match, "skill_match", 0),
    "experience_match": getattr(match, "experience_match", 0),
    "education_match": getattr(match, "education_match", 0),
    "resume_summary": analysis.summary,
    "recommendation": (
        "Strongly recommended" if getattr(match, "overall_match", 0) >= 75 else
        "Consider applying" if getattr(match, "overall_match", 0) >= 50 else
        "Not recommended"
    ),
    "matched_skills": getattr(match, "matched_skills", []),
    "missing_skills": getattr(match, "missing_skills", []),
    "resume_tips": analysis.resume_advice,
    "career_plan": getattr(analysis, "learning_plan", getattr(analysis, "career_plan", [])),
    "technical_questions": getattr(analysis, "technical_questions", []),
    "behavioral_questions": getattr(analysis, "behavioral_questions", []),
    "hr_questions": getattr(analysis, "hr_questions", [])
  }
  pdf_path = generate_pdf(report_data)

  with open(pdf_path, "rb") as pdf_file:
    pdf_bytes = pdf_file.read()

  st.download_button(
    label="📄 Download Complete Career Report",
    data=pdf_bytes,
    file_name="AI_Career_Report.pdf",
    mime="application/pdf",
    use_container_width=True,
)