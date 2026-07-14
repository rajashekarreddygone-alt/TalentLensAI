from src.ai.analysis import analyze_resume_ai

class AIService:

    @staticmethod
    def analyze_resume(resume_text):
        return analyze_resume_ai(resume_text)

    @staticmethod
    def generate_summary(resume_text):
        return analyze_resume_ai(resume_text).summary

    @staticmethod
    def generate_ats_feedback(resume_text):
        return analyze_resume_ai(resume_text).ats_feedback

    @staticmethod
    def generate_interview_questions(resume_text):
        analysis = analyze_resume_ai(resume_text)

        return {
            "technical": analysis.technical_questions,
            "behavioral": analysis.behavioral_questions,
            "hr": analysis.hr_questions,
        }