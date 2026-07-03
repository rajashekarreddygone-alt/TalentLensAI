from docx import Document


def extract_text_from_docx(docx_path):
    """
    Extract text from a DOCX resume.
    """

    document = Document(docx_path)

    text = ""

    for paragraph in document.paragraphs:
        text += paragraph.text + "\n"

    return text