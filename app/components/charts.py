import matplotlib.pyplot as plt
import os


def create_score_chart(report):

    labels = [
        "Skills",
        "Experience",
        "Education"
    ]

    scores = [
        report["skill_match"],
        report["experience_match"],
        report["education_match"]
    ]

    plt.figure(figsize=(6,4))

    bars = plt.bar(labels, scores)

    plt.ylim(0,100)

    plt.ylabel("Score (%)")

    plt.title("ATS Match Breakdown")

    for bar, score in zip(bars, scores):
        plt.text(
            bar.get_x()+bar.get_width()/2,
            score+2,
            f"{score:.0f}%",
            ha="center"
        )

    os.makedirs("reports", exist_ok=True)

    chart_path = "reports/ats_chart.png"

    plt.tight_layout()

    plt.savefig(chart_path)

    plt.close()

    return chart_path