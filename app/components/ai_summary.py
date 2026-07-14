import streamlit as st


def show_ai_summary(analysis):

    st.subheader("📄 AI Resume Summary")

    st.info(analysis.summary)