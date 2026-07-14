import re


def calculate_experience_score(text):

    years = re.findall(
        r"(\d+)\+?\s+years?",
        text.lower()
    )

    if len(years) == 0:
        return 20

    maximum = max(
        int(year)
        for year in years
    )

    return min(maximum * 20, 100)