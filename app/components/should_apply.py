import streamlit as st


def show_should_apply(match_result):
    """
    Displays AI recommendation on whether the candidate should apply.
    """

    score = match_result.overall_match

    if score >= 85:
        title = "🟢 Highly Recommended"
        color = "green"

        reasons = [
            "Excellent overall job match.",
            "Most required skills are already present.",
            "Experience strongly aligns with the role.",
            "Education requirements are satisfied.",
            "High probability of getting shortlisted."
        ]

    elif score >= 70:
        title = "🟡 Recommended"

        color = "orange"

        reasons = [
            "Good overall compatibility.",
            "A few important skills are missing.",
            "Resume is competitive for this position.",
            "Learning the missing skills will improve chances."
        ]

    elif score >= 50:
        title = "🟠 Apply After Improvements"

        color = "orange"

        reasons = [
            "Moderate job match.",
            "Several required skills are missing.",
            "Improve resume before applying.",
            "Complete recommended learning roadmap first."
        ]

    else:
        title = "🔴 Not Recommended"

        color = "red"

        reasons = [
            "Current profile does not closely match the job.",
            "Many important skills are missing.",
            "Experience does not satisfy the requirements.",
            "Consider another role or upskill first."
        ]

    st.markdown("---")

    st.header("🎯 Should You Apply?")

    st.success(title)

    st.metric(
        "Overall Job Compatibility Score",
        f"{score:.1f}%"
    )

    st.subheader("Why?")

    for reason in reasons:
        st.write("✅", reason)

    st.info(
        "This recommendation combines ATS score, skill matching, "
        "experience match, education match and semantic similarity."
    )