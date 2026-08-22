from pathlib import Path

from poml import poml

PROJECT_ROOT = Path(__file__).resolve().parents[1]
PROMPT_PATH = PROJECT_ROOT / "prompts" / "customer_support.poml"


def render_customer_support_prompt(
    customer_name: str,
    product_name: str,
) -> str:
    """Render the customer-support POML template."""

    context = {
        "customer_name": customer_name,
        "product_name": product_name,
    }

    return poml(
        PROMPT_PATH,
        context=context,
        format="dict",
    )


def main() -> None:
    rendered_prompt = render_customer_support_prompt(
        customer_name="Alex",
        product_name="Diamond Ring",
    )

    print("=" * 60)
    print("RENDERED POML PROMPT")
    print("=" * 60)
    print(rendered_prompt)


if __name__ == "__main__":
    main()