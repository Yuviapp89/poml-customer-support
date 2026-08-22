from pathlib import Path

from poml import poml


PROJECT_ROOT = Path(__file__).resolve().parents[1]
PROMPT_PATH = PROJECT_ROOT / "prompts" / "technical_advisor.poml"


def render_prompt(
    conversation_history: str,
    customer_name: str,
    application_name: str,
    environment: str,
    reference_context: str,
    customer_question: str,
) -> dict:
    """Render the technical advisor POML prompt."""

    context = {
        "conversation_history": conversation_history,
        "customer_name": customer_name,
        "application_name": application_name,
        "environment": environment,
        "reference_context": reference_context,
        "customer_question": customer_question,
    }

    return poml(
        PROMPT_PATH,
        context=context,
        format="dict",
    )


def main() -> None:
    result = render_prompt(
        conversation_history=(
            "Customer: The application cannot connect to PostgreSQL.\n"
            "Assistant: Let's check the database configuration.\n"
            "Customer: The error occurs during startup."
        ),
        customer_name="Alex",
        application_name="Customer Portal",
        environment="Development",
        reference_context=(
            "Database: PostgreSQL\n"
            "Known issue: Connection timeout"
        ),
        customer_question=(
            "What should I check first?"
        ),
    )

    for index, message in enumerate(
        result["messages"],
        start=1,
    ):
        print("=" * 70)
        print(f"MESSAGE {index}")
        print(f"SPEAKER: {message['speaker']}")
        print("-" * 70)
        print(message["content"])
        print()


if __name__ == "__main__":
    main()