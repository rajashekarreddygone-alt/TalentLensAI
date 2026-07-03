import re


def clean_text(text):
    """
    Clean resume text while preserving line structure.
    """

    text = text.replace("\xa0", " ")

    # Remove extra spaces but keep line breaks
    text = re.sub(r"[ \t]+", " ", text)

    # Collapse excessive blank lines
    text = re.sub(r"\n{2,}", "\n", text)

    return text.strip()