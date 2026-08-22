from pathlib import Path

from poml import poml


PROJECT_ROOT = Path(__file__).resolve().parents[1]
PROMPT_PATH = PROJECT_ROOT / "prompts" / "variables_demo.poml"


def render_prompt(
    customer_name: str,
    application_name: str,
    environment: str,
    issue_description: str,
) -> dict:

    context = {
        "customer_name": customer_name,
        "application_name": application_name,
        "environment": environment,
        "issue_description": issue_description,
    }

    return poml(
        PROMPT_PATH,
        context=context,
        format="dict",
    )


def main() -> None:
    result = render_prompt(
    customer_name="Alex",
    application_name="Customer Portal",
    environment="Development",
    issue_description="Database connection timeout",
)

    for message in result["messages"]:
        print("=" * 60)
        print(f"Speaker: {message['speaker']}")
        print(message["content"])


if __name__ == "__main__":
    main()