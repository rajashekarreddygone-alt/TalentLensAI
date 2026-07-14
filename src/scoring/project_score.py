import re


def calculate_project_score(text):

    count = len(
        re.findall(
            r"project",
            text.lower()
        )
    )

    return min(count * 25, 100)