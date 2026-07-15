import os
import sys
import streamlit as st

# -------------------------------------------------
# Add project root to Python path
# -------------------------------------------------

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

# -------------------------------------------------
# Page Configuration
# -------------------------------------------------

st.set_page_config(
    page_title="TalentLens AI",
    page_icon="🎯",
    layout="wide"
)

# -------------------------------------------------
# Main Header
# -------------------------------------------------

st.title("🎯 TalentLens AI")

st.subheader(
    "AI-Powered Resume Ranking & Interview Recommendation Platform"
)

st.markdown("---")

# -------------------------------------------------
# Introduction
# -------------------------------------------------

st.markdown("""
### Welcome to TalentLens AI

TalentLens AI is an AI-powered recruitment intelligence platform designed
to support both **recruiters** and **job candidates**.

The platform combines resume analysis, job-description matching,
candidate ranking, explainable recommendations, recruitment analytics,
and AI-powered career guidance to support more informed hiring and
career decisions.
""")

# -------------------------------------------------
# Recruiter Features
# -------------------------------------------------

st.markdown("### 👨‍💼 For Recruiters")

st.markdown("""
TalentLens AI helps recruiters:

- 📄 Parse and analyze multiple candidate resumes
- 🎯 Match candidates with job descriptions
- ⭐ Generate a **Recruiter Ranking Score**
- 📊 Rank and compare candidates
- 🔍 Search and filter candidates using advanced criteria
- ✅ Identify candidate strengths and weaknesses
- 💡 Generate explainable recruitment recommendations
- ⭐ Manage candidate shortlists
- 📝 Add recruiter notes and update candidate status
- ⚖️ Compare candidates side-by-side
- 🤖 Use an AI Recruiter Assistant for candidate insights
- 📈 Analyze recruitment trends through an analytics dashboard
- 📥 Generate downloadable candidate reports
""")

# -------------------------------------------------
# Candidate Features
# -------------------------------------------------

st.markdown("### 🎓 For Candidates")

st.markdown("""
TalentLens AI helps candidates:

- 📄 Upload and analyze their resume
- 🎯 Compare their resume with a selected job description
- 📊 Calculate a **Job Compatibility Score**
- ✅ Identify matched skills
- ❌ Identify missing skills
- 💼 Evaluate whether they should apply for a role
- 🤖 Receive AI-powered resume analysis
- 💡 Get personalized resume improvement suggestions
- 🛣️ Generate an AI-powered career roadmap
- 📚 Receive learning and course recommendations
- 💻 Discover recommended projects and career opportunities
- 🎯 Prepare with technical, behavioral, and HR interview questions
- 📥 Generate a downloadable career report
""")

# -------------------------------------------------
# Score Explanation
# -------------------------------------------------

st.markdown("### 📊 Intelligent Evaluation")

st.info("""
TalentLens AI uses different evaluation perspectives for recruiters and
candidates. The **Job Compatibility Score** measures how well a candidate's
resume aligns with a selected job description, while the **Recruiter Ranking
Score** provides a broader recruiter-focused evaluation using multiple
candidate assessment factors.
""")

# -------------------------------------------------
# Navigation
# -------------------------------------------------

st.markdown("---")

st.markdown("""
### 🚀 Get Started

Use the navigation menu on the left to explore:

**Recruiter** — Analyze, rank, compare, and manage candidates.

**Analytics** — View recruitment insights and candidate score distributions.

**Candidate** — Analyze job compatibility and receive personalized AI career guidance.

**About** — Learn more about TalentLens AI and the technologies used to build the platform.
""")

# -------------------------------------------------
# Project Status
# -------------------------------------------------

st.success("Project Status: Full Application Completed & Functional ✅")