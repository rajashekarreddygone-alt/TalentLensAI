from src.parser.resume_parser import parse_resume

from src.models.feature_vector import FeatureVector

from src.scoring.final_score import calculate_final_score

from src.explainability.explainer import generate_explanation


resume = parse_resume(
    "data/resumes/sample_resume.txt"
)

features = FeatureVector(
    semantic_score=82,
    skill_score=90,
    experience_score=60,
    education_score=80,
    project_score=90,
    certification_score=60,
    ats_score=95
)

score = calculate_final_score(features)

required_skills = [
    "Python",
    "SQL",
    "Machine Learning",
    "Docker",
    "AWS",
    "Kubernetes"
]

result = generate_explanation(
    resume,
    score,
    required_skills
)

print(result)