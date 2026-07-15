from dataclasses import dataclass


@dataclass
class ScoreResult:

    overall_score: float

    semantic_score: float

    skill_score: float

    experience_score: float

    education_score: float

    project_score: float

    certification_score: float

    ats_score: float