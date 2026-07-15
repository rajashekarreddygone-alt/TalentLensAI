import streamlit as st

from src.analytics.dashboard import generate_statistics

st.title("📊 TalentLens AI Analytics")

if "reports" not in st.session_state:

    st.warning("Analyze candidates first.")

    st.stop()

reports = st.session_state["reports"]

stats = generate_statistics(reports)

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "👥 Candidates",
    stats["candidate_count"]
)

col2.metric(
    "⭐ Average Score",
    f"{stats['average_score']}%"
)

col3.metric(
    "🏆 Highest Score",
    f"{stats['highest_score']}%"
)

col4.metric(
    "🔻 Lowest Score",
    f"{stats['lowest_score']}%"
)
import plotly.express as px

scores = [r.overall_score for r in reports]

fig = px.histogram(

    x=scores,

    nbins=10,

    title="Candidate Score Distribution"

)

st.plotly_chart(
    fig,
    use_container_width=True
)
recommendations = {}

for r in reports:

    recommendations[r.recommendation] = (

        recommendations.get(

            r.recommendation,

            0

        )

        + 1

    )

fig = px.pie(

    values=list(recommendations.values()),

    names=list(recommendations.keys()),

    title="Recommendation Distribution"

)

st.plotly_chart(
    fig,
    use_container_width=True
)
strengths = stats["strengths"]

fig = px.bar(

    x=list(strengths.keys()),

    y=list(strengths.values()),

    title="Most Common Strengths"

)

st.plotly_chart(
    fig,
    use_container_width=True
)
weaknesses = stats["weaknesses"]

fig = px.bar(

    x=list(weaknesses.keys()),

    y=list(weaknesses.values()),

    title="Most Common Weaknesses"

)

st.plotly_chart(
    fig,
    use_container_width=True
)
