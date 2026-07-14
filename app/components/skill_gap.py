import streamlit as st


def show_skill_gap(ai_result):

    roadmap = ai_result.career_roadmap

    st.markdown("---")
    st.header("🎯 Skill Gap Analysis")

    st.subheader("🔴 High Priority Skills")

    if roadmap.priority_skills:
        for skill in roadmap.priority_skills:
            st.error(skill)
    else:
        st.success("No critical skill gaps found.")

    st.markdown("---")

    st.subheader("📚 Suggested Learning Plan")

    if roadmap.weekly_plan:
        for week in roadmap.weekly_plan:
            st.info(week)

    st.success(
        f"Expected Match After Learning: {roadmap.expected_match_after_learning}"
    )