from string import Template


PROMPT_TEMPLATE = Template(
    """
You are an expert technical support assistant.

Task:
Help customers troubleshoot application issues.

Guidelines:
- Be concise.
- Don't invent information.
- State when information is insufficient.

Example:
Customer: API returns HTTP 401.
Assistant: Check the authentication credentials.

Current question:
$customer_question
""".strip()
)


def build_prompt(customer_question: str) -> str:
    return PROMPT_TEMPLATE.substitute(
        customer_question=customer_question
    )


def main() -> None:
    prompt = build_prompt(
        "My API returns HTTP 403. What should I check?"
    )

    print(prompt)


if __name__ == "__main__":
    main()