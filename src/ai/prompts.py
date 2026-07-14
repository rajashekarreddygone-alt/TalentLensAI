PROMPT = """
You are an expert technical recruiter.

Analyze the following resume.

Return:

1. Professional Summary

2. ATS Feedback

3. Resume Improvement Advice

4. Explain the ATS Score

5. Five Technical Interview Questions

6. Five Behavioral Interview Questions

7. Five HR Interview Questions


Resume

------------------------

{resume}

"""
# Renamed to avoid overwriting the earlier PROMPT and to ensure string literals are terminated correctly
CAREER_COACH_PROMPT = PROMPT

PROMPT = """
You are an experienced AI career coach.

Given:

1. Candidate Resume
2. Job Description
3. Missing Skills

Generate JSON only.

{
  "priority_skills":[
      {
        "skill":"",
        "priority":"",
        "reason":"",
        "learning_time":""
      }
  ],

  "learning_roadmap":[
      {
        "week":"",
        "focus":"",
        "topics":[]
      }
  ],

  "recommended_courses":[
      {
        "course":"",
        "provider":"",
        "reason":""
      }
  ],

  "recommended_projects":[
      {
        "title":"",
        "difficulty":"",
        "skills":[]
      }
  ],

  "recommended_certifications":[
      {
        "name":"",
        "provider":""
      }
  ],

  "career_paths":[
      ""
  ],

  "expected_match_after_learning":"",
  "estimated_learning_duration":""
}
"""