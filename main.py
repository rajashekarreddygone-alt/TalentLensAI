from src.parser.resume_parser import parse_resume


resume = parse_resume("data/resumes/sample_resume.txt")


print("\nCandidate Information\n")

print(f"Name          : {resume.name}")
print(f"Email         : {resume.email}")
print(f"Phone         : {resume.phone}")
print(f"Skills        : {resume.skills}")