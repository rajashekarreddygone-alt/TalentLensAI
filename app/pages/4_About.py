import streamlit as st

# -------------------------------------------------
# Page Configuration
# -------------------------------------------------

st.set_page_config(
    page_title="About | TalentLens AI",
    page_icon="ℹ️",
    layout="wide"
)

# -------------------------------------------------
# Main Header
# -------------------------------------------------

st.title("ℹ️ About TalentLens AI")

st.markdown("""
**TalentLens AI** is an AI-powered recruitment intelligence platform
designed to support both recruiters and job candidates.

The platform combines resume parsing, semantic job matching, candidate
ranking, explainable recommendations, recruitment analytics, and
AI-powered career guidance to support data-driven recruitment and
career decisions.
""")

st.markdown("---")

# -------------------------------------------------
# Key Features
# -------------------------------------------------

st.header("🚀 Key Features")

st.markdown("""
### 👨‍💼 Recruiter Features

- 📄 **Resume Parsing** — Extract and analyze information from candidate resumes.
- 🎯 **Semantic Resume–Job Matching** — Evaluate alignment between resumes and job descriptions.
- ⭐ **Recruiter Candidate Ranking** — Rank candidates using a Recruiter Ranking Score.
- 🔍 **Advanced Search & Filtering** — Filter candidates based on score, recommendation, and required skills.
- 💡 **Explainable Recommendations** — Display candidate strengths, weaknesses, and areas for improvement.
- ⭐ **Shortlist Management** — Manage shortlisted candidates for the recruitment process.
- 📝 **Recruiter Notes & Status Tracking** — Record notes and track candidate recruitment status.
- ⚖️ **Candidate Comparison** — Compare candidates side-by-side using relevant evaluation criteria.
- 🤖 **AI Recruiter Assistant** — Ask questions about analyzed candidates and receive AI-powered insights.
- 📊 **Recruitment Analytics** — Visualize candidate scores, recommendations, strengths, and weaknesses.
- 📥 **Candidate Reports** — Generate downloadable candidate evaluation reports.

### 🎓 Candidate Features

- 📄 **Resume Analysis** — Upload and analyze a resume against a selected job description.
- 🎯 **Job Compatibility Scoring** — Measure resume-job alignment using a Job Compatibility Score.
- ✅ **Skill Match Analysis** — Identify skills that match the job requirements.
- ❌ **Missing Skill Detection** — Highlight important skills that may need improvement.
- 💼 **Application Recommendation** — Help candidates understand whether they should consider applying.
- 🤖 **AI Resume Analysis** — Generate AI-powered insights about resume-job alignment.
- 💡 **Resume Improvement Suggestions** — Provide personalized suggestions to strengthen the resume.
- 🛣️ **AI Career Roadmap** — Recommend priority skills and a structured learning plan.
- 📚 **Learning Recommendations** — Suggest relevant courses and learning areas.
- 💻 **Project Recommendations** — Suggest practical projects for skill development.
- 🚀 **Career Opportunities** — Identify potential career paths based on the candidate profile.
- 🎯 **Interview Preparation** — Generate technical, behavioral, and HR interview questions.
- 📥 **Career Reports** — Generate a downloadable career analysis report.
""")

st.markdown("---")

# -------------------------------------------------
# Evaluation Approach
# -------------------------------------------------

st.header("📊 Evaluation Approach")

st.markdown("""
TalentLens AI provides different evaluation perspectives for recruiters
and candidates.

The **Job Compatibility Score** in the Candidate Dashboard measures how
well a candidate's resume aligns with a selected job description based
on factors such as skills, experience, education, keyword coverage, and
semantic similarity.

The **Recruiter Ranking Score** provides a broader recruiter-focused
evaluation using multiple candidate assessment factors. This allows
recruiters to compare and prioritize candidates while allowing candidates
to independently understand their compatibility with a specific role.

Because these scores serve different purposes, the Job Compatibility Score
and Recruiter Ranking Score may differ for the same candidate.
""")

st.markdown("---")

# -------------------------------------------------
# How It Works
# -------------------------------------------------

st.header("⚙️ How TalentLens AI Works")

st.markdown("""
**For Recruiters:**  
Recruiters upload a job description and multiple candidate resumes.
TalentLens AI analyzes the candidates, evaluates resume-job alignment,
generates recruiter-focused ranking scores, and provides recommendations,
strengths, weaknesses, and candidate insights. Recruiters can then search,
filter, compare, shortlist, and manage candidates.

**For Candidates:**  
Candidates upload their resume and provide a job description. TalentLens AI
evaluates job compatibility, identifies matched and missing skills, and
provides personalized AI-powered career guidance, resume improvement
suggestions, learning recommendations, and interview preparation support.

**AI-Powered Insights:**  
The platform uses AI-assisted analysis to generate career roadmaps,
resume feedback, interview questions, and recruiter decision-support
insights. Career roadmap recommendations may include broader long-term
development areas beyond skills directly missing from a specific job
description.
""")

st.markdown("---")

# -------------------------------------------------
# Technology Stack
# -------------------------------------------------

st.header("🛠️ Technology Stack")

st.markdown("""
TalentLens AI is built using:

- 🐍 **Python** — Core application and backend logic
- 🎈 **Streamlit** — Interactive web application and dashboard interface
- 🤖 **Machine Learning & Natural Language Processing** — Resume and job-description analysis
- 🧠 **Sentence Transformers** — Semantic similarity and resume-job matching
- 🔤 **spaCy** — Natural language processing and text analysis
- 📊 **Scikit-learn** — Machine learning and similarity-based evaluation
- 📈 **Plotly** — Interactive recruitment analytics and data visualization
""")

st.markdown("---")

# -------------------------------------------------
# Project Objective
# -------------------------------------------------

st.header("🎯 Project Objective")

st.markdown("""
The objective of TalentLens AI is to demonstrate how Artificial Intelligence,
Machine Learning, Natural Language Processing, and semantic matching can be
combined to create an intelligent recruitment support platform.

The system is designed to improve transparency in candidate evaluation by
providing explainable scores, strengths, weaknesses, skill-gap analysis,
and recommendations rather than relying only on a single ranking value.

TalentLens AI is intended as a recruitment decision-support and career-guidance
platform. Final hiring decisions should remain with human recruiters and
organizations.
""")

# -------------------------------------------------
# Project Status
# -------------------------------------------------

st.markdown("---")

st.success("Project Status: Full Application Completed & Functional ✅")