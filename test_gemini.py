from src.ai.resume_summary import generate_resume_summary

resume = """
John Doe

Python
Machine Learning
Deep Learning
TensorFlow
PyTorch

Worked on NLP projects.

3 years experience.

Master's Degree in Computer Science.
"""

summary = generate_resume_summary(resume)

print(summary)