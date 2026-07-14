from io import BytesIO

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
)


def generate_report(candidate_name, report_data):

    buffer = BytesIO()

    doc = SimpleDocTemplate(buffer)

    styles = getSampleStyleSheet()

    story = []

    story.append(
        Paragraph(
            "<b><font size=20>TalentLens AI Career Report</font></b>",
            styles["Title"],
        )
    )

    story.append(Spacer(1, 20))

    story.append(
        Paragraph(
            f"<b>Candidate:</b> {candidate_name}",
            styles["Normal"],
        )
    )

    story.append(Spacer(1, 12))

    story.append(
        Paragraph(
            f"<b>Overall Match:</b> {report_data.get('overall_match',0)}%",
            styles["Normal"],
        )
    )

    story.append(
        Paragraph(
            f"<b>Recommendation:</b> {report_data.get('recommendation','N/A')}",
            styles["Normal"],
        )
    )

    story.append(Spacer(1,20))

    story.append(
        Paragraph(
            "<b>AI Resume Summary</b>",
            styles["Heading2"],
        )
    )

    story.append(
        Paragraph(
            report_data.get("resume_summary",""),
            styles["BodyText"],
        )
    )

    if report_data.get("ats_feedback"):

        story.append(Spacer(1,15))

        story.append(
            Paragraph(
                "<b>ATS Feedback</b>",
                styles["Heading2"],
            )
        )

        story.append(
            Paragraph(
                report_data["ats_feedback"],
                styles["BodyText"],
            )
        )

    if report_data.get("score_explanation"):

        story.append(Spacer(1,15))

        story.append(
            Paragraph(
                "<b>Score Explanation</b>",
                styles["Heading2"],
            )
        )

        story.append(
            Paragraph(
                report_data["score_explanation"],
                styles["BodyText"],
            )
        )

    if report_data.get("resume_advice"):

        story.append(Spacer(1,15))

        story.append(
            Paragraph(
                "<b>Resume Improvement Suggestions</b>",
                styles["Heading2"],
            )
        )

        for tip in report_data["resume_advice"]:
            story.append(
                Paragraph(
                    "• " + tip,
                    styles["BodyText"],
                )
            )

    doc.build(story)

    buffer.seek(0)

    return buffer