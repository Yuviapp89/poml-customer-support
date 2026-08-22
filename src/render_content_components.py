from pathlib import Path

from poml import poml


PROJECT_ROOT = Path(__file__).resolve().parents[1]
PROMPT_PATH = PROJECT_ROOT / "prompts" / "content_components_demo.poml"


def render_prompt() -> dict:
    """Render the M1.3 content-components demonstration."""

    return poml(
        PROMPT_PATH,
        format="dict",
    )


def main() -> None:
    result = render_prompt()

    for index, message in enumerate(result["messages"], start=1):
        print(f"\n{'=' * 60}")
        print(f"MESSAGE {index}")
        print(f"{'=' * 60}")
        print(f"Speaker: {message['speaker']}")
        print(message["content"])


if __name__ == "__main__":
    main()