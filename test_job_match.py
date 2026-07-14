"""
Test Script for Job Match Engine

Run:
python test_job_match.py
"""

from dataclasses import dataclass

from src.matching.job_matcher import calculate_job_match


# ------------------------------------------------------------------
# Mock Resume Object
# ------------------------------------------------------------------

@dataclass
class MockResume:
    skills: list
    experience: str = ""
    education: str = ""


# ------------------------------------------------------------------
# Mock Job Description Object
# ------------------------------------------------------------------

@dataclass
class MockJob:
    skills: list
    experience: str = ""
    education: str = ""


# ------------------------------------------------------------------
# Sample Resume
# ------------------------------------------------------------------

resume = MockResume(
    skills=[
        "Python",
        "Machine Learning",
        "TensorFlow",
        "SQL",
        "Git",
        "Pandas",
        "NumPy",
    ],
    experience="2 years",
    education="Bachelor's Degree",
)

# ------------------------------------------------------------------
# Sample Job Description
# ------------------------------------------------------------------

job = MockJob(
    skills=[
        "Python",
        "TensorFlow",
        "Docker",
        "AWS",
        "SQL",
        "Machine Learning",
    ],
    experience="2 years",
    education="Bachelor's Degree",
)

# ------------------------------------------------------------------
# Calculate Match
# ------------------------------------------------------------------

result = calculate_job_match(resume, job)

# ------------------------------------------------------------------
# Display Results
# ------------------------------------------------------------------

print("=" * 60)
print("JOB MATCH RESULTS")
print("=" * 60)

print(f"\nOverall Match        : {result.overall_match:.2f}%")
print(f"Skill Match          : {result.skill_match:.2f}%")
print(f"Semantic Similarity  : {result.semantic_similarity:.2f}%")
print(f"Experience Match     : {result.experience_match:.2f}%")
print(f"Education Match      : {result.education_match:.2f}%")
print(f"Keyword Coverage     : {result.keyword_coverage:.2f}%")

print("\n" + "=" * 60)
print("MATCHED SKILLS")
print("=" * 60)

for skill in result.matched_skills:
    print(f"✅ {skill}")

print("\n" + "=" * 60)
print("MISSING SKILLS")
print("=" * 60)

for skill in result.missing_skills:
    print(f"❌ {skill}")

print("\n" + "=" * 60)
print("RECOMMENDED TO LEARN")
print("=" * 60)

for skill in result.recommended_skills:
    print(f"📘 {skill}")

print("\n" + "=" * 60)
print("TEST COMPLETED SUCCESSFULLY")
print("=" * 60)