from src.render_context_separation import render_prompt


def test_context_is_separated_from_instructions() -> None:
    result = render_prompt(
        application_name="Test Portal",
        database="PostgreSQL",
        environment="Testing",
        known_issue="Connection timeout",
        customer_question="What should I check first?",
    )

    messages = result["messages"]

    assert len(messages) == 2

    system_content = messages[0]["content"]
    human_content = messages[1]["content"]

    assert "Response Guidelines" in system_content
    assert "Test Portal" in human_content
    assert "PostgreSQL" in human_content
    assert "What should I check first?" in human_content
    #assert "Somebody watching me is my anxiety" in human_content