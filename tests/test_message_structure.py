from src.render_message_structure import render_prompt


def test_message_sequence() -> None:
    result = render_prompt(customer_question="What should I check first?")

    speakers = [
        message["speaker"]
        for message in result["messages"]
    ]

    assert speakers == [
        "system",
        "human",
        "ai",
        "human",
    ]