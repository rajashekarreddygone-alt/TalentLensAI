from src.parser.skills_extractor import extract_skills


def parse_job_description(text: str):

    skills = extract_skills(text)

    return {
        "text": text,
        "skills": skills
    }