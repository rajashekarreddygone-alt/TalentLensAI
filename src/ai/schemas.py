from pydantic import BaseModel


# ---------- Career Roadmap Models ----------

class PrioritySkill(BaseModel):
    skill: str
    priority: str
    reason: str
    learning_time: str


class WeeklyPlan(BaseModel):
    week: str
    focus: str
    topics: list[str]


class Course(BaseModel):
    course: str
    provider: str
    reason: str


class Project(BaseModel):
    title: str
    difficulty: str
    skills: list[str]


class Certification(BaseModel):
    name: str
    provider: str


class CareerRoadmap(BaseModel):
    priority_skills: list[str]
    weekly_plan: list[str]
    recommended_courses: list[str]
    recommended_projects: list[str]
    career_paths: list[str]
    expected_match_after_learning: str


# ---------- Main Analysis Model ----------

class ResumeAnalysis(BaseModel):

    summary: str

    ats_feedback: str

    resume_advice: list[str]

    score_explanation: str

    technical_questions: list[str]

    behavioral_questions: list[str]

    hr_questions: list[str]

    career_roadmap: CareerRoadmap