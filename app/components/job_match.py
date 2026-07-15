import streamlit as st


def display_job_match(result):

    if result is None:
        return

    st.markdown("---")
    st.header("🎯 Job Match Analysis")

    score = result.overall_match

    st.metric(
        "Job Compatibility Score",
        f"{score:.2f}%"
    )

    st.progress(min(score / 100, 1.0))

    st.markdown("### Match Breakdown")

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Skill Match",
        f"{result.skill_match:.2f}%"
    )

    c2.metric(
        "Experience",
        f"{result.experience_match:.2f}%"
    )

    c3.metric(
        "Education",
        f"{result.education_match:.2f}%"
    )

    st.markdown("---")

    st.subheader("✅ Matched Skills")

    if result.matched_skills:

        cols = st.columns(3)

        for i, skill in enumerate(result.matched_skills):
            cols[i % 3].success(skill)

    else:
        st.info("No matched skills.")

    st.subheader("❌ Missing Skills")

    if result.missing_skills:

        cols = st.columns(3)

        for i, skill in enumerate(result.missing_skills):
            cols[i % 3].error(skill)

    else:
        st.success("No missing skills.")

    st.markdown("---")

    if score >= 85:
        st.success("🟢 Highly Recommended")

    elif score >= 70:
        st.warning("🟡 Recommended")

    else:
        st.error("🔴 Needs Improvement")