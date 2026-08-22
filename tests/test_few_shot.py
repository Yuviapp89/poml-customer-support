from src.render_few_shot import render_prompt


def test_few_shot_structure() -> None:
    result = render_prompt(
        customer_question="My application returns HTTP 403."
    )

    speakers = [
        message["speaker"]
        for message in result["messages"]
    ]

    assert speakers == [
        "system",
        "human",
        "ai",
        "human",
        "ai",
        "human",
    ]


def test_current_question_is_dynamic() -> None:
    result = render_prompt(
        customer_question="My API returns HTTP 500."
    )

    final_message = result["messages"][-1]

    assert final_message["speaker"] == "human"
    assert "HTTP 500" in final_message["content"]