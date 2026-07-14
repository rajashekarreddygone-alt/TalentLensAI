from src.ai.analysis import analyze_resume_ai

resume = """
John Doe

Python
Machine Learning
Deep Learning
TensorFlow
PyTorch

3 years experience

Master Degree

NLP Projects
"""

analysis = analyze_resume_ai(resume)

print()

print("SUMMARY")
print("--------------------------------")
print(analysis.summary)

print()

print("ATS FEEDBACK")
print("--------------------------------")
print(analysis.ats_feedback)

print()

print("SCORE EXPLANATION")
print("--------------------------------")
print(analysis.score_explanation)

print()

print("RESUME ADVICE")
print("--------------------------------")

for item in analysis.resume_advice:
    print("-", item)

print()

print("TECHNICAL QUESTIONS")
print("--------------------------------")

for q in analysis.technical_questions:
    print("-", q)

print()

print("BEHAVIORAL QUESTIONS")
print("--------------------------------")

for q in analysis.behavioral_questions:
    print("-", q)

print()

print("HR QUESTIONS")
print("--------------------------------")

for q in analysis.hr_questions:
    print("-", q)