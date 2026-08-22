def build_prompt(customer_question: str) -> str:
    return f"""
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
{customer_question}
""".strip()


def main() -> None:
    prompt = build_prompt(
        "My API returns HTTP 403. What should I check?"
    )

    print(prompt)


if __name__ == "__main__":
    main()