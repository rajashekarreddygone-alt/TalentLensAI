import os

from src.models.resume import Resume
from src.parser.pdf_parser import extract_text_from_pdf
from src.parser.docx_parser import extract_text_from_docx
from src.parser.text_cleaner import clean_text
from src.parser.entity_extractor import (
    extract_email,
    extract_phone,
    extract_name
)
from src.parser.skills_extractor import extract_skills


def parse_resume(file_path):

    extension = os.path.splitext(file_path)[1].lower()

    if extension == ".pdf":

        text = extract_text_from_pdf(file_path)

    elif extension == ".docx":

        text = extract_text_from_docx(file_path)

    elif extension == ".txt":

        with open(file_path, "r", encoding="utf-8") as file:
            text = file.read()

    else:
        raise ValueError("Unsupported file type")

    text = clean_text(text)

    resume = Resume(
        name=extract_name(text),
        email=extract_email(text),
        phone=extract_phone(text),
        skills=extract_skills(text),
        raw_text=text,
    )

    return resume