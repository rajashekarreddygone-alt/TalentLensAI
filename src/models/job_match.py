from dataclasses import dataclass, field


@dataclass
class JobMatchResult:
    overall_match: float

    skill_match: float

    semantic_similarity: float

    experience_match: float

    education_match: float

    keyword_coverage: float

    matched_skills: list = field(default_factory=list)

    missing_skills: list = field(default_factory=list)

    recommended_skills: list = field(default_factory=list)