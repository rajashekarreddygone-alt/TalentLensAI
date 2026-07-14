from src.parser.job_parser import parse_job_description

with open(
    "data/job_descriptions/ml_engineer.txt",
    "r",
    encoding="utf-8"
) as f:

    jd = f.read()

result = parse_job_description(jd)

print(result)