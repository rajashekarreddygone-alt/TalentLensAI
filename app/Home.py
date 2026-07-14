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

st.set_page_config(
    page_title="TalentLens AI",
    page_icon="🎯",
    layout="wide"
)

st.title("🎯 TalentLens AI")

st.subheader(
    "AI-Powered Resume Ranking & Interview Recommendation Platform"
)

st.markdown("---")

st.markdown("""
Welcome to TalentLens AI.

This platform helps recruiters:

- Parse resumes
- Match candidates with job descriptions
- Rank applicants intelligently
- Explain recommendations
- Generate interview questions
- Analyze hiring insights

Use the navigation menu on the left to begin.
""")

st.success("Project Status: Backend Completed ✅")