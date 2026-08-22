from pathlib import Path

from poml import poml


PROJECT_ROOT = Path(__file__).resolve().parents[1]
PROMPT_PATH = PROJECT_ROOT / "prompts" / "output_requirements_demo.poml"


def render_prompt(customer_question: str) -> dict:
    context = {
        "customer_question": customer_question,
    }

    return poml(
        PROMPT_PATH,
        context=context,
        format="dict",
    )


def main() -> None:
    result = render_prompt(
    customer_question="My API returns HTTP 403. What should I check?"
)

    for index, message in enumerate(result["messages"], start=1):
        print("=" * 60)
        print(f"MESSAGE {index}")
        print(f"SPEAKER: {message['speaker']}")
        print(message["content"])


if __name__ == "__main__":
    main()