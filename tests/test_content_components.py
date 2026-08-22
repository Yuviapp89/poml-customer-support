from pathlib import Path

from poml import poml


PROJECT_ROOT = Path(__file__).resolve().parents[1]
PROMPT_PATH = PROJECT_ROOT / "prompts" / "content_components_demo.poml"


def test_content_components_render() -> None:
    result = poml(
        PROMPT_PATH,
        format="dict",
    )

    assert "messages" in result
    assert len(result["messages"]) == 2

    system_message = result["messages"][0]
    human_message = result["messages"][1]

    assert system_message["speaker"] == "system"
    assert human_message["speaker"] == "human"

    assert "Troubleshooting Steps" in system_message["content"]
    assert "database connection error" in human_message["content"]