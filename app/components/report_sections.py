from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.colors import HexColor
from reportlab.platypus import Paragraph, Spacer

styles = getSampleStyleSheet()

title_style = styles["Heading1"]
title_style.textColor = HexColor("#1E88E5")
title_style.alignment = TA_CENTER

heading_style = styles["Heading2"]
heading_style.textColor = HexColor("#1565C0")

body_style = styles["BodyText"]

def title(text):
    return [
        Paragraph(text, title_style),
        Spacer(1,20)
    ]

def heading(text):
    return [
        Paragraph(text, heading_style),
        Spacer(1,10)
    ]

def body(text):
    return [
        Paragraph(text, body_style),
        Spacer(1,12)
    ]