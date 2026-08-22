from pathlib import Path

from poml import poml


PROJECT_ROOT = Path(__file__).resolve().parents[1]
PROMPT_PATH = PROJECT_ROOT / "prompts" / "context_separation_demo.poml"


def render_prompt(
    application_name: str,
    database: str,
    environment: str,
    known_issue: str,
    customer_question: str,
) -> dict:

    context = {
        "application_name": application_name,
        "database": database,
        "environment": environment,
        "known_issue": known_issue,
        "customer_question": customer_question,
    }

    return poml(
        PROMPT_PATH,
        context=context,
        format="dict",
    )


def main() -> None:
    result = render_prompt(
        application_name="Customer Portal",
        database="PostgreSQL",
        environment="Development",
        known_issue="Database connection timeout",
        customer_question="What should I check first?",
    )

    for index, message in enumerate(result["messages"], start=1):
        print("=" * 60)
        print(f"MESSAGE {index}")
        print(f"SPEAKER: {message['speaker']}")
        print(message["content"])


if __name__ == "__main__":
    main()