import streamlit as st


def show_interview_questions(analysis):

    st.subheader("🎯 Technical Questions")

    for q in analysis.technical_questions:

        st.write("•", q)

    st.divider()

    st.subheader("🤝 Behavioral Questions")

    for q in analysis.behavioral_questions:

        st.write("•", q)

    st.divider()

    st.subheader("💼 HR Questions")

    for q in analysis.hr_questions:

        st.write("•", q)