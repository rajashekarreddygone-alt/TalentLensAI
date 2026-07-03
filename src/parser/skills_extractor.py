from src.parser.constants import SKILLS


def extract_skills(text):
    """
    Extract known skills from resume.
    """

    found_skills = []

    lower_text = text.lower()

    for skill in SKILLS:

        if skill.lower() in lower_text:
            found_skills.append(skill)

    return sorted(list(set(found_skills)))