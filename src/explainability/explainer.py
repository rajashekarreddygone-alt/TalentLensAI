from src.models.resume import Resume
from src.models.score_result import ScoreResult


def generate_explanation(
    resume: Resume,
    score: ScoreResult,
    required_skills: list
):

    strengths = []

    weaknesses = []

    recommendations = []

    # Skill Analysis
    for skill in required_skills:

        if skill in resume.skills:
            strengths.append(f"{skill} matched")

        else:
            weaknesses.append(f"Missing {skill}")

    # Experience
    if score.experience_score >= 60:
        strengths.append("Relevant experience")

    else:
        weaknesses.append("Limited experience")

    # ATS
    if score.ats_score >= 80:
        strengths.append("ATS friendly resume")

    else:
        recommendations.append("Improve ATS formatting")

    # Overall Recommendation
    if score.overall_score >= 85:

        hiring = "Highly Recommended"

    elif score.overall_score >= 70:

        hiring = "Recommended"

    else:

        hiring = "Needs Improvement"

    return {

        "overall": score.overall_score,

        "strengths": strengths,

        "weaknesses": weaknesses,

        "recommendation": hiring,

        "improvements": recommendations
    }