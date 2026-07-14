from src.models.job_match import JobMatchResult
from src.config import JOB_MATCH_WEIGHTS


def _normalize(items):
    return {item.strip().lower() for item in items if item}


def calculate_job_match(resume, job):

    resume_skills = _normalize(resume.skills)
    job_skills = _normalize(job.skills)

    matched = sorted(resume_skills & job_skills)
    missing = sorted(job_skills - resume_skills)

    if job_skills:
        skill_match = (len(matched) / len(job_skills)) * 100
    else:
        skill_match = 100

    # Placeholder values for now
    semantic_similarity = skill_match
    experience_match = 100
    education_match = 100
    keyword_coverage = skill_match

    overall = (
        skill_match * JOB_MATCH_WEIGHTS["skill_match"]
        + semantic_similarity * JOB_MATCH_WEIGHTS["semantic_similarity"]
        + experience_match * JOB_MATCH_WEIGHTS["experience_match"]
        + education_match * JOB_MATCH_WEIGHTS["education_match"]
        + keyword_coverage * JOB_MATCH_WEIGHTS["keyword_coverage"]
    )

    return JobMatchResult(
        overall_match=round(overall, 2),
        skill_match=round(skill_match, 2),
        semantic_similarity=round(semantic_similarity, 2),
        experience_match=round(experience_match, 2),
        education_match=round(education_match, 2),
        keyword_coverage=round(keyword_coverage, 2),
        matched_skills=matched,
        missing_skills=missing,
        recommended_skills=missing,
    )