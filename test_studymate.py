
from search_notes import search_notes


def test_requirements_analysis():
    result = search_notes("What is requirements analysis?")

    assert "identifies what users need" in result.lower()
    print("PASS: Requirements analysis search")


def test_empty_question():
    result = search_notes("the is a")

    assert "more specific question" in result.lower()
    print("PASS: Empty or vague question")


def test_no_matching_information():
    result = search_notes("quantum physics")

    assert "no matching information" in result.lower()
    print("PASS: No matching information")


if __name__ == "__main__":
    test_requirements_analysis()
    test_empty_question()
    test_no_matching_information()

    print("\nAll tests passed!")
