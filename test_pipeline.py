from src.pipeline.candidate_pipeline import analyze_candidate

with open(
    "data/job_descriptions/ml_engineer.txt",
    "r",
    encoding="utf-8"
) as f:

    jd = f.read()

required_skills = [
    "Python",
    "SQL",
    "Machine Learning",
    "Docker",
    "AWS",
    "Kubernetes"
]

candidate = analyze_candidate(
    "data/resumes/sample_resume.txt",
    jd,
    required_skills
)

print(candidate)