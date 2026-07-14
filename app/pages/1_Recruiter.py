import os
import sys

PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..")
)

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

import streamlit as st

from src.pipeline.candidate_pipeline import analyze_candidate
from src.utils.file_handler import save_uploaded_file
from src.parser.job_parser import parse_job_description
from pdf_generator import generate_candidate_report

st.title("👨‍💼 Recruiter Dashboard")

job_description = st.file_uploader(
    "Upload Job Description",
    type=["txt"]
)

resumes = st.file_uploader(
    "Upload Resumes",
    type=["pdf", "docx"],
    accept_multiple_files=True
)
reports = []
if st.button("Analyze Candidates"):

    if job_description is None:

        st.error("Please upload a Job Description.")

    elif len(resumes) == 0:

        st.error("Please upload resumes.")

    else:

        jd_text = job_description.read().decode("utf-8")

        job = parse_job_description(jd_text)

        required_skills = job["skills"]

        reports = []

        for uploaded_resume in resumes:

            resume_path = save_uploaded_file(uploaded_resume)

            report = analyze_candidate(
                resume_path,
                jd_text,
                required_skills
            )

            reports.append(report)

        reports.sort(
            key=lambda x: x.overall_score,
            reverse=True
        )
        st.session_state["reports"] = reports
        st.success("Analysis Completed!")
        st.subheader("Required Skills")

        st.subheader("🎯 Required Skills")

        cols = st.columns(4)

        for i, skill in enumerate(required_skills):
            cols[i % 4].success(skill)

        candidate_count = len(reports)

        average_score = round(
            sum(r.overall_score for r in reports) / candidate_count,
            2
        )

        recommended = sum(r.recommendation == "Recommended" for r in reports)
        highly = sum(r.recommendation == "Highly Recommended" for r in reports)

        col1, col2, col3, col4 = st.columns(4)

        col1.metric("👥 Candidates", candidate_count)
        col2.metric("⭐ Average Score", f"{average_score}%")
        col3.metric("🟢 Highly Recommended", highly)
        col4.metric("🟡 Recommended", recommended)

        top = reports[0]

        st.success(
            f"""
🏆 Best Candidate

Name : {top.name}

Overall Score : {top.overall_score:.2f}%

Recommendation : {top.recommendation}
"""
        )

        st.subheader("Candidate Rankings")

        table = []
        for report in reports:
            if report.recommendation == "Highly Recommended":
                badge = "🟢 Highly Recommended"
            elif report.recommendation == "Recommended":
                badge = "🟡 Recommended"
            else:
                badge = "🔴 Needs Improvement"

            table.append({
                "Candidate": report.name,
                "Overall Score": f"{report.overall_score:.2f}%",
                "Recommendation": badge
            })

        st.dataframe(table, use_container_width=True)

        st.subheader("Candidate Details")

        for report in reports:
            with st.expander(report.name):
                st.metric("Overall Score", f"{report.overall_score:.2f}%")
                st.progress(report.overall_score / 100, text=f"{report.overall_score:.2f}% Match")

                st.write("### Strengths")
                for item in report.strengths:
                    st.success(item)

                st.write("### Weaknesses")
                for item in report.weaknesses:
                    st.error(item)

                st.write("### Improvements")
                if report.improvements:
                    for item in report.improvements:
                        st.warning(item)
                else:
                    st.info("No improvements suggested.")
                
                pdf_filename = f"{report.name.replace(' ', '_')}_Report.pdf"

                generate_candidate_report(report, pdf_filename)

                with open(pdf_filename, "rb") as pdf_file:
                 st.download_button(
                 label="📄 Download PDF Report",
                  data=pdf_file,
                   file_name=pdf_filename,
                   mime="application/pdf",
                    key=f"pdf_{report.name}"
                    )

        