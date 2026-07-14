import re


def extract_email(text):
    """
    Extract email address.
    """

    pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"

    match = re.search(pattern, text)

    if match:
        return match.group()

    return None


def extract_phone(text):
    """
    Extract Indian phone number.
    """

    pattern = r"(\+91[-\s]?)?[6-9]\d{9}"

    match = re.search(pattern, text)

    if match:
        return match.group()

    return None


import spacy

nlp = spacy.load("en_core_web_sm")


def extract_name(text):
    """
    Extract candidate name using spaCy Named Entity Recognition.
    """

    doc = nlp(text)

    for entity in doc.ents:
        if entity.label_ == "PERSON":
            return entity.text.split("\n")[0].strip()

    return None