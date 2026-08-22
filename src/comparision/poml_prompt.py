from pathlib import Path

from poml import poml


PROJECT_ROOT = Path(__file__).resolve().parents[2]
PROMPT_PATH = PROJECT_ROOT / "prompts" / "comparison_demo.poml"


def build_prompt(customer_question: str) -> dict:
    context = {
        "customer_question": customer_question,
    }

    return poml(
        PROMPT_PATH,
        context=context,
        format="dict",
    )


def main() -> None:
    result = build_prompt(
        "My API returns HTTP 403. What should I check?"
    )

    for message in result["messages"]:
        print("=" * 60)
        print(f"Speaker: {message['speaker']}")
        print(message["content"])


if __name__ == "__main__":
    main()