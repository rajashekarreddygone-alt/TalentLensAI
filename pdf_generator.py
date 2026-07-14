from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.colors import green, red, orange


def generate_candidate_report(report, filename):
    c = canvas.Canvas(filename, pagesize=letter)

    width, height = letter

    y = height - 50

    c.setFont("Helvetica-Bold", 22)
    c.drawString(50, y, "TalentLens AI")
    y -= 35

    c.setFont("Helvetica-Bold", 18)
    c.drawString(50, y, "Candidate Evaluation Report")
    y -= 40

    c.setFont("Helvetica", 12)

    c.drawString(50, y, f"Candidate : {report.name}")
    y -= 25

    c.drawString(50, y, f"Email : {report.email}")
    y -= 25

    c.drawString(50, y, f"Phone : {report.phone}")
    y -= 40

    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, y, "Scores")
    y -= 25

    c.setFont("Helvetica", 12)

    c.drawString(60, y, f"Semantic Score : {report.semantic_score:.2f}")
    y -= 20

    c.drawString(60, y, f"Skill Score : {report.skill_score:.2f}")
    y -= 20

    c.drawString(60, y, f"Experience Score : {report.experience_score:.2f}")
    y -= 20

    c.drawString(60, y, f"Education Score : {report.education_score:.2f}")
    y -= 20

    c.drawString(60, y, f"Project Score : {report.project_score:.2f}")
    y -= 20

    c.drawString(60, y, f"Certification Score : {report.certification_score:.2f}")
    y -= 35

    c.setFont("Helvetica-Bold", 16)

    if report.overall_score >= 80:
        c.setFillColor(green)
    elif report.overall_score >= 60:
        c.setFillColor(orange)
    else:
        c.setFillColor(red)

    c.drawString(
        50,
        y,
        f"Overall Score : {report.overall_score:.2f}%"
    )

    y -= 30

    c.setFillColor(red)
    c.drawString(50, y, f"Recommendation : {report.recommendation}")

    y -= 40

    c.setFillColor(green)

    c.setFont("Helvetica-Bold", 15)
    c.drawString(50, y, "Strengths")
    y -= 25

    c.setFont("Helvetica", 12)

    for strength in report.strengths:
        c.drawString(70, y, "• " + strength)
        y -= 18

    y -= 20

    c.setFillColor(red)

    c.setFont("Helvetica-Bold", 15)
    c.drawString(50, y, "Weaknesses")
    y -= 25

    c.setFont("Helvetica", 12)

    for weakness in report.weaknesses:
        c.drawString(70, y, "• " + weakness)
        y -= 18

    y -= 20

    c.setFillColor(orange)

    c.setFont("Helvetica-Bold", 15)
    c.drawString(50, y, "Suggestions")
    y -= 25

    c.setFont("Helvetica", 12)

    for item in report.improvements:
        c.drawString(70, y, "• " + item)
        y -= 18

    c.save()