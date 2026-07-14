import streamlit as st


def show_resume_advice(analysis):

    st.subheader("💡 Resume Improvement Suggestions")

    for advice in analysis.resume_advice:

        st.success(advice)