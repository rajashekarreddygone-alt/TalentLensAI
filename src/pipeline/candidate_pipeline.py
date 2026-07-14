from src.parser.resume_parser import parse_resume
from src.matching.similarity import calculate_similarity

from src.scoring.skill_score import calculate_skill_score
from src.scoring.experience_score import calculate_experience_score
from src.scoring.education_score import calculate_education_score
from src.scoring.project_score import calculate_project_score
from src.scoring.certification_score import calculate_certification_score
from src.scoring.ats_score import calculate_ats_score

from src.models.feature_vector import FeatureVector
from src.scoring.final_score import calculate_final_score

from src.explainability.explainer import generate_explanation

from src.models.candidate_report import CandidateReport
def analyze_candidate(
    resume_path,
    job_description_text,
    required_skills,
):
    resume = parse_resume(resume_path)
    semantic = calculate_similarity(
    resume.raw_text,
    job_description_text
)

    semantic = round(semantic * 100, 2)
    skill = calculate_skill_score(
        resume.skills,
        required_skills
    )
    experience = calculate_experience_score(
        resume.raw_text
    )
    education = calculate_education_score(
        resume.raw_text
    )
    projects = calculate_project_score(
        resume.raw_text
    )
    certifications = calculate_certification_score(
        resume.raw_text
    )
    ats = calculate_ats_score(
        resume
    )
    features = FeatureVector(
        semantic_score=semantic,
        skill_score=skill,
        experience_score=experience,
        education_score=education,
        project_score=projects,
        certification_score=certifications,
        ats_score=ats,
    )
    score = calculate_final_score(
        features
    )
    explanation = generate_explanation(
        resume,
        score,
        required_skills
    )
    if score.overall_score >= 85:
        recommendation = "Highly Recommended"
    elif score.overall_score >= 70:
        recommendation = "Recommended"
    else:
        recommendation = "Needs Improvement"

    return CandidateReport(
        name=resume.name,
        email=resume.email,
        phone=resume.phone,
        semantic_score=semantic,
        skill_score=skill,
        experience_score=experience,
        education_score=education,
        project_score=projects,
        certification_score=certifications,
        ats_score=ats,
        overall_score=score.overall_score,
        recommendation=recommendation,
        strengths=explanation["strengths"],
        weaknesses=explanation["weaknesses"],
        improvements=explanation["improvements"],
    )

