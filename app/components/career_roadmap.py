import streamlit as st


def show_career_roadmap(ai_result):

    roadmap = ai_result.career_roadmap

    st.markdown("---")
    st.header("🎓 AI Career Roadmap")

    # -----------------------
    # Priority Skills
    # -----------------------
    st.subheader("🎯 Priority Skills")

    if roadmap.priority_skills:
        for skill in roadmap.priority_skills:
            st.warning(f"📌 {skill}")
    else:
        st.success("No priority skills identified.")

    # -----------------------
    # Weekly Learning Plan
    # -----------------------
    st.subheader("📅 Learning Plan")

    if roadmap.weekly_plan:
        for week in roadmap.weekly_plan:
            st.info(week)

    # -----------------------
    # Recommended Courses
    # -----------------------
    st.subheader("📚 Recommended Courses")

    if roadmap.recommended_courses:
        for course in roadmap.recommended_courses:
            st.success(course)

    # -----------------------
    # Recommended Projects
    # -----------------------
    st.subheader("💻 Recommended Projects")

    if roadmap.recommended_projects:
        for project in roadmap.recommended_projects:
            st.success(project)

    # -----------------------
    # Career Opportunities
    # -----------------------
    st.subheader("🚀 Career Opportunities")

    if roadmap.career_paths:
        for path in roadmap.career_paths:
            st.info(path)

    # -----------------------
    # Final Prediction
    # -----------------------
    st.metric(
        "Expected Match After Learning",
        roadmap.expected_match_after_learning,
    )