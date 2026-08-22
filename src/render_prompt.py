from pathlib import Path
from poml import poml

PROJECT_ROOT = Path(__file__).resolve().parents[1]
PROMPT_PATH = PROJECT_ROOT / "prompts" / "content_components_demo.poml"

def render_prompt() -> dict:
    return poml(
        PROMPT_PATH,
        format="dict",
    )

def main() -> None:
    result = render_prompt()

    for message in result["messages"]:
        print("-" * 50)
        print(f"Speaker : {message['speaker']}")
        print(f"Content : {message['content']}")

if __name__ == "__main__":
    main()