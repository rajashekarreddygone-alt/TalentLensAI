import re


def calculate_certification_score(text):

    count = len(
        re.findall(
            r"certification|certificate",
            text.lower()
        )
    )

    return min(count * 20, 100)