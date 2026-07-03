from src.parser.resume_parser import parse_resume


def test_parser():

    resume = parse_resume("data/resumes/sample_resume.txt")

    assert resume.email is not None

    assert len(resume.skills) > 0

    print("Parser Test Passed")


if __name__ == "__main__":

    test_parser()