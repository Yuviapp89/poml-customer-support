from pathlib import Path

from poml import poml


PROJECT_ROOT = Path(__file__).resolve().parents[1]
PROMPT_PATH = PROJECT_ROOT / "prompts" / "role_instruction_demo.poml"


def render_prompt() -> dict:
    """Render the POML conversation into structured messages."""

    return poml(
        PROMPT_PATH,
        format="openai_chat",
    )


def main() -> None:
    result = render_prompt()
    print(result)

    # print("Messages:")
    # for message in result["messages"]:
    #     print("-" * 50)
    #     print(f"Speaker : {message['speaker']}")
    #     print(f"Content : {message['content']}")


if __name__ == "__main__":
    main()