from collections import Counter


def generate_statistics(reports):

    scores = [r.overall_score for r in reports]

    strengths = []

    weaknesses = []

    for r in reports:

        strengths.extend(r.strengths)

        weaknesses.extend(r.weaknesses)

    return {

        "candidate_count": len(reports),

        "average_score": round(sum(scores) / len(scores), 2),

        "highest_score": max(scores),

        "lowest_score": min(scores),

        "strengths": Counter(strengths),

        "weaknesses": Counter(weaknesses)

    }