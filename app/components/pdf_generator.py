from reportlab.platypus import *
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_CENTER
from reportlab.platypus import Image
from app.components.charts import create_score_chart
from app.components.report_sections import *

styles = getSampleStyleSheet()


def generate_pdf(report):

    filename = "reports/AI_Career_Report.pdf"

    doc = SimpleDocTemplate(
        filename,
        pagesize=(8.27*inch,11.69*inch)
    )

    story=[]
    from reportlab.lib.units import mm


    def add_page_number(canvas, doc):
        canvas.saveState()
        canvas.setFont("Helvetica",9)
        canvas.drawString(
            20*mm,
            10*mm,
            f"TalentLens AI | Page {doc.page}"
        )
        canvas.restoreState()

    # ---------------------------------------
    # COVER PAGE
    # ---------------------------------------

    cover_style = styles["Heading1"]
    cover_style.alignment = TA_CENTER
    cover_style.textColor = HexColor("#1565C0")
    cover_style.fontSize=28

    story.append(Spacer(1,1.8*inch))

    story.append(
        Paragraph(
            "TalentLens AI",
            cover_style
        )
    )

    story.append(Spacer(1,20))

    story.append(
        Paragraph(
            "Complete Career Analysis Report",
            styles["Title"]
        )
    )

    story.append(Spacer(1,30))

    story.append(
        Paragraph(
            f"<b>Candidate:</b> {report['candidate_name']}",
            styles["Heading2"]
        )
    )

    story.append(Spacer(1,10))

    story.append(
        Paragraph(
            f"<b>Overall Match:</b> {report['overall_match']}%",
            styles["Heading2"]
        )
    )

    story.append(PageBreak())

    # ---------------------------------------
    # SUMMARY
    # ---------------------------------------

    story += heading("Executive Summary")

    story += body(report["resume_summary"])

    story += heading("Recommendation")

    story += body(report["recommendation"])

    story.append(PageBreak())

    # ---------------------------------------
    # ATS SCORE
    # ---------------------------------------

    story += heading("ATS Analysis")

    table_data = [

        ["Category","Score"],

        ["Overall",str(report["overall_match"])+"%"],

        ["Skills",str(report["skill_match"])+"%"],

        ["Experience",str(report["experience_match"])+"%"],

        ["Education",str(report["education_match"])+"%"],

    ]

    table=Table(table_data)

    table.setStyle(TableStyle([

        ("BACKGROUND",(0,0),(-1,0),HexColor("#1565C0")),

        ("TEXTCOLOR",(0,0),(-1,0),"white"),

        ("GRID",(0,0),(-1,-1),1,"grey"),

        ("BACKGROUND",(0,1),(-1,-1),HexColor("#F4F8FF")),

        ("BOTTOMPADDING",(0,0),(-1,0),10),

    ]))

    story.append(table)

    story.append(PageBreak())
    chart = create_score_chart(report)

    story.append(Spacer(1,20))

    story.append(
    Image(
        chart,
        width=420,
        height=280
    )
 )

    story.append(PageBreak())

    

    # ---------------------------------------
    # MATCHED SKILLS
    # ---------------------------------------

    story += heading("Missing Skills")

    missing_table = [["Missing Skills"]]

    for skill in report["missing_skills"]:
        missing_table.append([skill])

    table = Table(missing_table)

    table.setStyle(TableStyle([
        ("BACKGROUND",(0,0),(-1,0),HexColor("#C62828")),
        ("TEXTCOLOR",(0,0),(-1,0),"white"),
        ("GRID",(0,0),(-1,-1),0.5,"grey"),
        ("BACKGROUND",(0,1),(-1,-1),HexColor("#FFEBEE"))
    ]))

    story.append(table)
    story.append(PageBreak())

    story += heading("Matched Skills")

    skill_table = [["Matched Skills"]]

    for skill in report["matched_skills"]:
        skill_table.append([skill])

    table = Table(skill_table)

    table.setStyle(TableStyle([

        ("BACKGROUND",(0,0),(-1,0),HexColor("#2E7D32")),

        ("TEXTCOLOR",(0,0),(-1,0),"white"),

        ("GRID",(0,0),(-1,-1),0.5,"grey"),

        ("BACKGROUND",(0,1),(-1,-1),HexColor("#E8F5E9"))

    ]))

    story.append(table)
    story.append(Spacer(1,20))
    story.append(PageBreak())

    # ---------------------------------------
    # RESUME IMPROVEMENTS
    # ---------------------------------------

    story += heading("Resume Improvement Suggestions")

    for tip in report["resume_tips"]:
        story += body("• "+tip)

    story.append(PageBreak())

    # ---------------------------------------
    # CAREER ROADMAP
    # ---------------------------------------

    story += heading("Career Roadmap")

    for step in report["career_plan"]:
        story += body(step)

    story.append(PageBreak())

    # ---------------------------------------
    # INTERVIEW QUESTIONS
    # ---------------------------------------

    story += heading("Technical Questions")

    for q in report["technical_questions"]:
        story += body("• "+q)

    story += heading("Behavioral Questions")

    for q in report["behavioral_questions"]:
        story += body("• "+q)

    story += heading("HR Questions")

    for q in report["hr_questions"]:
        story += body("• "+q)

    doc.build(
    story,
    onFirstPage=add_page_number,
    onLaterPages=add_page_number
 )

    return filename