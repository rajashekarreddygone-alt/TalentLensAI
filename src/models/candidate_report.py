from dataclasses import dataclass, field


@dataclass
class CandidateReport:

    # Candidate Information
    name: str
    email: str
    phone: str

    # Individual Scores
    semantic_score: float
    skill_score: float
    experience_score: float
    education_score: float
    project_score: float
    certification_score: float
    ats_score: float
    overall_score: float

    # Final Recommendation
    recommendation: str

    # Existing Explainability
    strengths: list = field(default_factory=list)
    weaknesses: list = field(default_factory=list)
    improvements: list = field(default_factory=list)

    # -------------------------
    # AI Features
    # -------------------------

    ai_summary: str = ""

    ai_resume_advice: str = ""

    ai_ats_feedback: str = ""

    ai_score_explanation: str = ""

    interview_questions: str = ""