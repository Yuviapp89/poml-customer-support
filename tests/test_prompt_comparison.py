from src.comparison.plain_python import build_prompt as build_plain_prompt
from src.comparison.python_template import build_prompt as build_template_prompt
from src.comparison.poml_prompt import build_prompt as build_poml_prompt


QUESTION = "My API returns HTTP 403. What should I check?"


def test_plain_python_contains_question() -> None:
    result = build_plain_prompt(QUESTION)

    assert QUESTION in result


def test_template_contains_question() -> None:
    result = build_template_prompt(QUESTION)

    assert QUESTION in result


def test_poml_contains_question() -> None:
    result = build_poml_prompt(QUESTION)

    contents = "\n".join(
        message["content"]
        for message in result["messages"]
    )

    assert QUESTION in contents