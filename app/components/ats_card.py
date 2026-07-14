import streamlit as st


def show_ats_card(analysis):

    st.subheader("📊 ATS Analysis")

    st.write("### ATS Feedback")

    st.success(analysis.ats_feedback)

    st.write("### Score Explanation")

    st.info(analysis.score_explanation)