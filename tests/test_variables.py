from src.render_variables import render_prompt


def test_variables_are_rendered() -> None:
    result = render_prompt(
        customer_name="Test User",
        application_name="Test Application",
        environment="Testing",
        issue_description="Connection timeout",
    )

    messages = result["messages"]

    combined_content = "\n".join(
        message["content"]
        for message in messages
    )

    assert "Test User" in combined_content
    assert "Test Application" in combined_content
    assert "Testing" in combined_content
    assert "Connection timeout" in combined_content