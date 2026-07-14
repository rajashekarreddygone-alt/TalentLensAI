def calculate_skill_score(
    resume_skills,
    required_skills
):
    """
    Percentage of required skills found.
    """

    if len(required_skills) == 0:
        return 100

    matched = 0

    resume_lower = {
        skill.lower()
        for skill in resume_skills
    }

    for skill in required_skills:

        if skill.lower() in resume_lower:
            matched += 1

    score = matched / len(required_skills)

    return round(score * 100, 2)