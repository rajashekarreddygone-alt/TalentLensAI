from src.config import (
    SEMANTIC_WEIGHT,
    SKILL_WEIGHT,
    EXPERIENCE_WEIGHT,
    EDUCATION_WEIGHT,
    PROJECT_WEIGHT,
    CERTIFICATION_WEIGHT,
    ATS_WEIGHT,
)

from src.models.feature_vector import FeatureVector
from src.models.score_result import ScoreResult


def calculate_final_score(features: FeatureVector) -> ScoreResult:

    overall = (
        features.semantic_score * SEMANTIC_WEIGHT
        + features.skill_score * SKILL_WEIGHT
        + features.experience_score * EXPERIENCE_WEIGHT
        + features.education_score * EDUCATION_WEIGHT
        + features.project_score * PROJECT_WEIGHT
        + features.certification_score * CERTIFICATION_WEIGHT
        + features.ats_score * ATS_WEIGHT
    )

    return ScoreResult(
        overall_score=round(overall, 2),
        semantic_score=features.semantic_score,
        skill_score=features.skill_score,
        experience_score=features.experience_score,
        education_score=features.education_score,
        project_score=features.project_score,
        certification_score=features.certification_score,
        ats_score=features.ats_score,
    )