def calculate_ats_score(resume):

    score = 100

    if resume.email == "":
        score -= 20

    if resume.phone == "":
        score -= 20

    if len(resume.skills) == 0:
        score -= 20

    if len(resume.projects) == 0:
        score -= 20

    if len(resume.education) == 0:
        score -= 20

    return score