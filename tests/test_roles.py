from pathlib import Path

from poml import poml


PROJECT_ROOT = Path(__file__).resolve().parents[1]
PROMPT_PATH = PROJECT_ROOT / "prompts" / "technical_support.poml"


def test_conversation_has_expected_speakers() -> None:
    result = poml(
        PROMPT_PATH,
        format="dict",
    )

    speakers = [message["speaker"] for message in result["messages"]]

    assert "system" in speakers
    assert "human" in speakers
    assert "ai" in speakers