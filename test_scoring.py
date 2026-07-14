from src.models.feature_vector import FeatureVector
from src.scoring.final_score import calculate_final_score

features = FeatureVector(
    semantic_score=82,
    skill_score=90,
    experience_score=60,
    education_score=80,
    project_score=90,
    certification_score=60,
    ats_score=95,
)

result = calculate_final_score(features)

print("\nTalentLens AI Score Report\n")
print(f"Overall Score      : {result.overall_score}")
print(f"Semantic Score     : {result.semantic_score}")
print(f"Skill Score        : {result.skill_score}")
print(f"Experience Score   : {result.experience_score}")
print(f"Education Score    : {result.education_score}")
print(f"Project Score      : {result.project_score}")
print(f"Certification Score: {result.certification_score}")
print(f"ATS Score          : {result.ats_score}")