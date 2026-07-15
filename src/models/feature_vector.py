from dataclasses import dataclass


@dataclass
class FeatureVector:

    semantic_score: float

    skill_score: float

    experience_score: float

    education_score: float

    project_score: float

    certification_score: float

    ats_score: float