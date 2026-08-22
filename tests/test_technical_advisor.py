from src.render_technical_advisor import render_prompt


def test_technical_advisor_structure() -> None:
    result = render_prompt(
        conversation_history="Previous conversation",
        customer_name="Test User",
        application_name="Test Application",
        environment="Testing",
        reference_context="Database: PostgreSQL",
        customer_question="What should I check?",
    )

    messages = result["messages"]

    assert len(messages) == 4

    speakers = [
        message["speaker"]
        for message in messages
    ]

    assert speakers == [
        "system",
        "human",
        "ai",
       # "human",
       # "ai",
       # "human",
    ]


def test_dynamic_context_is_rendered() -> None:
    result = render_prompt(
        conversation_history="Previous conversation",
        customer_name="Test User",
        application_name="Test Application",
        environment="Testing",
        reference_context="Database: PostgreSQL",
        customer_question="What should I check?",
    )

    final_message = result["messages"][-1]["content"]

    assert "Test User" in final_message
    assert "Test Application" in final_message
    assert "Testing" in final_message
    assert "Database: PostgreSQL" in final_message
    assert "What should I check?" in final_message