def calculate_education_score(text):

    text = text.lower()

    if "phd" in text:
        return 100

    if "m.tech" in text or "masters" in text:
        return 90

    if "b.tech" in text:
        return 80

    if "b.sc" in text:
        return 70

    return 50