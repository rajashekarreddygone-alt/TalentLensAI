from src.parser.resume_parser import parse_resume
from src.matching.similarity import calculate_similarity


resume = parse_resume("data/resumes/sample_resume.txt")

with open(
    "data/job_descriptions/ml_engineer.txt",
    "r",
    encoding="utf-8"
) as file:
    job_description = file.read()

score = calculate_similarity(
    resume.raw_text,
    job_description
)

print(f"\nSemantic Similarity Score: {score:.2f}")