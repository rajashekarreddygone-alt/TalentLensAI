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
from src.ai.recruiter_assistant import ask_recruiter_assistant
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

if "reports" not in st.session_state:
    st.session_state["reports"] = []

if "required_skills" not in st.session_state:
    st.session_state["required_skills"] = []

if "shortlisted_candidates" not in st.session_state:
    st.session_state["shortlisted_candidates"] = []

if "candidate_status" not in st.session_state:
    st.session_state["candidate_status"] = {}

if "recruiter_notes" not in st.session_state:
    st.session_state["recruiter_notes"] = {}


def build_recruiter_assistant_context():
    """
    Build structured candidate context for the AI Recruiter Assistant
    using the analyzed reports and recruiter-managed information.
    """

    all_reports = st.session_state.get("reports", [])

    if not all_reports:
        return ""

    context_parts = []

    for report in all_reports:
        status = st.session_state["candidate_status"].get(
            report.name,
            "New"
        )

        recruiter_note = st.session_state["recruiter_notes"].get(
            report.name,
            "No recruiter notes available."
        )

        is_shortlisted = (
            report.name
            in st.session_state["shortlisted_candidates"]
        )

        candidate_context = f"""
Candidate Name: {report.name}
Overall Score: {report.overall_score:.2f}%
Recommendation: {report.recommendation}
Status: {status}
Shortlisted: {"Yes" if is_shortlisted else "No"}
Strengths: {", ".join(report.strengths) if report.strengths else "None"}
Weaknesses: {", ".join(report.weaknesses) if report.weaknesses else "None"}
Improvements: {", ".join(report.improvements) if report.improvements else "None"}
Recruiter Notes: {recruiter_note}
"""

        context_parts.append(candidate_context)

    return "\n--------------------\n".join(context_parts)

reports = st.session_state["reports"]
required_skills = st.session_state["required_skills"]

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
        st.session_state["required_skills"] = required_skills

reports = st.session_state["reports"]
required_skills = st.session_state["required_skills"]

for report in reports:
        if report.name not in st.session_state["candidate_status"]:
            st.session_state["candidate_status"][report.name] = "New"

if reports:
        st.success("Analysis Completed!")
        st.divider()
        st.subheader("🔍 Search & Advanced Filters")

        search_name = st.text_input(
            "Search Candidate",
            placeholder="Enter candidate name..."
        )

        col1, col2, col3 = st.columns(3)

        with col1:
            min_score = st.slider(
                "Minimum Score",
                0,
                100,
                0
            )

        with col2:
            recommendation_filter = st.selectbox(
                "Recommendation",
                [
                    "All",
                    "Highly Recommended",
                    "Recommended",
                    "Needs Improvement"
                ]
            )

        with col3:
            skill_filter = st.selectbox(
                "Required Skill",
                ["All"] + required_skills
            )

        st.subheader("🎯 Required Skills")

        cols = st.columns(4)
        for i, skill in enumerate(required_skills):
            cols[i % 4].success(skill)

        filtered_reports = []
        for report in reports:
            if search_name:
                if search_name.lower() not in report.name.lower():
                    continue

            if report.overall_score < min_score:
                continue

            if recommendation_filter != "All":
                if report.recommendation != recommendation_filter:
                    continue

            if skill_filter != "All":
                matched = any(
                    skill_filter.lower() in strength.lower()
                    for strength in report.strengths
                )

                if not matched:
                    continue

            filtered_reports.append(report)

        reports = filtered_reports
        candidate_count = len(reports)
        average_score = round(
            sum(r.overall_score for r in reports) / candidate_count,
            2
        ) if candidate_count > 0 else 0

        recommended = sum(r.recommendation == "Recommended" for r in reports)
        highly = sum(r.recommendation == "Highly Recommended" for r in reports)

        col1, col2, col3, col4 = st.columns(4)
        col1.metric("👥 Candidates", candidate_count)
        col2.metric("⭐ Average Score", f"{average_score}%")
        col3.metric("🟢 Highly Recommended", highly)
        col4.metric("🟡 Recommended", recommended)

        if reports:
            top = reports[0]
            st.success(
                f"""
🏆 Best Candidate

Name : {top.name}

Recruiter Ranking Score : {top.overall_score:.2f}%

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

            candidate_status = st.session_state["candidate_status"].get(report.name, "New")

            table.append({
                "Candidate": report.name,
                "Recruiter Ranking Score": f"{report.overall_score:.2f}%",
                "Recommendation": badge,
                "Status": candidate_status
            })

        st.dataframe(table, use_container_width=True)
        st.caption(
    "Recruiter Ranking Score provides a broader evaluation of each candidate "
    "using multiple recruitment factors, including resume-job alignment and "
    "additional candidate evaluation criteria. It may differ from the "
    "Job Compatibility Score shown in the Candidate Dashboard."
)

        st.subheader("Candidate Details")
        status_options = [
            "New",
            "Reviewing",
            "Shortlisted",
            "Interview Scheduled",
            "Selected",
            "Rejected"
        ]
        def update_candidate_status(candidate_name):
         st.session_state["candidate_status"][candidate_name] = (
          st.session_state[f"status_{candidate_name}"]
         )

        for report in reports:
            with st.expander(report.name):
                st.metric("Recruiter Ranking Score", f"{report.overall_score:.2f}%")

                current_status = st.session_state["candidate_status"].get(report.name, "New")

                selected_status = st.selectbox(
                 "Candidate Status",
                  status_options,
                 index=status_options.index(current_status),
                  key=f"status_{report.name}",
                   on_change=update_candidate_status,
                 args=(report.name,)
                )
                st.write("### 📝 Recruiter Notes")

                current_note = st.session_state["recruiter_notes"].get(
                    report.name,
                    ""
                )

                recruiter_note = st.text_area(
                    "Add notes about this candidate",
                    value=current_note,
                    placeholder="Example: Strong technical background. Consider for technical interview.",
                    key=f"note_{report.name}"
                )

                if st.button(
                    "💾 Save Note",
                    key=f"save_note_{report.name}"
                ):
                    st.session_state["recruiter_notes"][report.name] = recruiter_note
                    st.success("Recruiter note saved successfully!")

                is_shortlisted = report.name in st.session_state["shortlisted_candidates"]

                if is_shortlisted:
                    if st.button("❌ Remove from Shortlist", key=f"remove_shortlist_{report.name}"):
                        st.session_state["shortlisted_candidates"].remove(report.name)
                        st.rerun()

                    st.success("⭐ This candidate is shortlisted")
                else:
                    if st.button("⭐ Add to Shortlist", key=f"add_shortlist_{report.name}"):
                        st.session_state["shortlisted_candidates"].append(report.name)
                        st.rerun()

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
        st.divider()

        st.subheader("⭐ Recruiter Shortlist Manager")

        shortlisted_names = st.session_state["shortlisted_candidates"]

        if shortlisted_names:

            st.write(
                f"**Total Shortlisted Candidates: {len(shortlisted_names)}**"
            )

            all_reports = st.session_state["reports"]

            shortlisted_reports = [
                report
                for report in all_reports
                if report.name in shortlisted_names
            ]

            shortlisted_reports.sort(
                key=lambda x: x.overall_score,
                reverse=True
            )

            shortlist_table = []

            for report in shortlisted_reports:

                if report.recommendation == "Highly Recommended":
                    badge = "🟢 Highly Recommended"

                elif report.recommendation == "Recommended":
                    badge = "🟡 Recommended"

                else:
                    badge = "🔴 Needs Improvement"

                candidate_status = st.session_state["candidate_status"].get(
                    report.name,
                    "New"
                )

                shortlist_table.append({
                    "Candidate": report.name,
                    "Recruiter Ranking Score": f"{report.overall_score:.2f}%",
                    "Recommendation": badge,
                    "Status": candidate_status
                })

            st.dataframe(
                shortlist_table,
                use_container_width=True
            )

        else:

            st.info(
                "No candidates have been shortlisted yet. "
                "Open a candidate's details and click 'Add to Shortlist'."
            )
                    # --------------------------------------------------
        # Candidate Comparison
        # --------------------------------------------------

        st.divider()

        st.subheader("⚖️ Candidate Comparison")

        all_reports = st.session_state["reports"]

        if len(all_reports) >= 2:

            candidate_names = [
                report.name
                for report in all_reports
            ]

            compare_col1, compare_col2 = st.columns(2)

            with compare_col1:
                candidate_1_name = st.selectbox(
                    "Select First Candidate",
                    candidate_names,
                    index=0,
                    key="compare_candidate_1"
                )

            with compare_col2:
                candidate_2_name = st.selectbox(
                    "Select Second Candidate",
                    candidate_names,
                    index=1,
                    key="compare_candidate_2"
                )

            if candidate_1_name == candidate_2_name:

                st.warning(
                    "Please select two different candidates for comparison."
                )

            else:

                candidate_1 = next(
                    report
                    for report in all_reports
                    if report.name == candidate_1_name
                )

                candidate_2 = next(
                    report
                    for report in all_reports
                    if report.name == candidate_2_name
                )

                st.write("### 📊 Side-by-Side Comparison")

                col1, col2 = st.columns(2)

                with col1:

                    st.write(f"## {candidate_1.name}")

                    st.metric(
                        "Recruiter Ranking Score",
                        f"{candidate_1.overall_score:.2f}%"
                    )

                    st.write(
                        f"**Recommendation:** "
                        f"{candidate_1.recommendation}"
                    )

                    candidate_1_status = st.session_state[
                        "candidate_status"
                    ].get(
                        candidate_1.name,
                        "New"
                    )

                    st.write(
                        f"**Status:** {candidate_1_status}"
                    )

                    if candidate_1.name in st.session_state[
                        "shortlisted_candidates"
                    ]:
                        st.success("⭐ Shortlisted")
                    else:
                        st.info("Not Shortlisted")

                    st.write("#### Strengths")

                    for strength in candidate_1.strengths:
                        st.success(strength)

                    st.write("#### Weaknesses")

                    for weakness in candidate_1.weaknesses:
                        st.error(weakness)

                    st.write("#### Improvements")

                    if candidate_1.improvements:
                        for improvement in candidate_1.improvements:
                            st.warning(improvement)
                    else:
                        st.info("No improvements suggested.")

                    st.write("#### 📝 Recruiter Notes")

                    candidate_1_note = st.session_state[
                        "recruiter_notes"
                    ].get(
                        candidate_1.name,
                        ""
                    )

                    if candidate_1_note:
                        st.info(candidate_1_note)
                    else:
                        st.info("No recruiter notes available.")

                with col2:

                    st.write(f"## {candidate_2.name}")

                    st.metric(
                        "Recruiter Ranking Score",
                        f"{candidate_2.overall_score:.2f}%"
                    )

                    st.write(
                        f"**Recommendation:** "
                        f"{candidate_2.recommendation}"
                    )

                    candidate_2_status = st.session_state[
                        "candidate_status"
                    ].get(
                        candidate_2.name,
                        "New"
                    )

                    st.write(
                        f"**Status:** {candidate_2_status}"
                    )

                    if candidate_2.name in st.session_state[
                        "shortlisted_candidates"
                    ]:
                        st.success("⭐ Shortlisted")
                    else:
                        st.info("Not Shortlisted")

                    st.write("#### Strengths")

                    for strength in candidate_2.strengths:
                        st.success(strength)

                    st.write("#### Weaknesses")

                    for weakness in candidate_2.weaknesses:
                        st.error(weakness)

                    st.write("#### Improvements")

                    if candidate_2.improvements:
                        for improvement in candidate_2.improvements:
                            st.warning(improvement)
                    else:
                        st.info("No improvements suggested.")

                    st.write("#### 📝 Recruiter Notes")

                    candidate_2_note = st.session_state[
                        "recruiter_notes"
                    ].get(
                        candidate_2.name,
                        ""
                    )

                    if candidate_2_note:
                        st.info(candidate_2_note)
                    else:
                        st.info("No recruiter notes available.")

        else:

            st.info(
                "At least two analyzed candidates are required "
                "to use Candidate Comparison."
            )

        # ============================================================
# AI RECRUITER ASSISTANT
# ============================================================

        st.divider()

        st.subheader("🤖 AI Recruiter Assistant")

        st.write(
            "Ask questions about the analyzed candidates. "
            "The AI assistant uses candidate scores, strengths, weaknesses, "
            "recommendations, recruitment status, shortlist information, "
            "and recruiter notes."
        )

        recruiter_question = st.text_area(
            "Ask the AI Recruiter Assistant",
            placeholder=(
                "Examples:\n"
                "• Who is the best candidate and why?\n"
                "• Compare the top two candidates.\n"
                "• Which candidate has the strongest technical skills?\n"
                "• Who should be considered for a technical interview?"
            ),
            key="recruiter_assistant_question"
        )

        if st.button(
            "🤖 Ask AI Recruiter Assistant",
            key="ask_recruiter_assistant_button"
        ):
            if not recruiter_question.strip():
                st.warning("Please enter a question for the AI Recruiter Assistant.")

            else:
                candidate_context = build_recruiter_assistant_context()

                if not candidate_context:
                    st.warning(
                        "No analyzed candidate data is available. "
                        "Please analyze candidates first."
                    )

                else:
                    with st.spinner("AI Recruiter Assistant is analyzing candidates..."):
                        assistant_response = ask_recruiter_assistant(
                            recruiter_question,
                            candidate_context
                        )

                    st.session_state["recruiter_assistant_response"] = (
                        assistant_response
                    )


        if st.session_state.get("recruiter_assistant_response"):
            st.markdown("### 💡 AI Assistant Response")

            st.info(
                st.session_state["recruiter_assistant_response"]
            )
                 