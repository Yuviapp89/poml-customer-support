# POML Customer Support Assistant

A hands-on AI Engineer learning project demonstrating Prompt
Orchestration Markup Language (POML) with Python and an LLM.

## Current Phase

M1 — POML Prompt Design & Rendering Patterns

## Objectives

- Set up a Python virtual environment
- Install the POML Python SDK
- Configure VS Code for POML
- Create standalone `.poml` prompt files
- Render POML from Python
- Pass dynamic context into POML
- Compare plain Python, string templates, and POML for prompt building
- Explore POML features: roles, message structure, few-shot examples,
  context separation, content components, and output requirements
- Add basic automated tests

## Project Structure

```text
poml-customer-support/
├── prompts/
│   ├── comparison_demo.poml
│   ├── content_components_demo.poml
│   ├── context_separation_demo.poml
│   ├── customer_support.poml
│   ├── few_shot_demo.poml
│   ├── message_structure_demo.poml
│   ├── output_requirements_demo.poml
│   ├── poml_prompt.py
│   ├── role_instruction_demo.poml
│   ├── technical_advisor.poml
│   ├── technical_support.poml
│   └── variables_demo.poml
├── src/
│   ├── __init__.py
│   ├── render_content_components.py
│   ├── render_context_separation.py
│   ├── render_few_shot.py
│   ├── render_message_structure.py
│   ├── render_output_requirements.py
│   ├── render_prompt.py
│   ├── render_roles.py
│   ├── render_technical_advisor.py
│   ├── render_variables.py
│   └── comparison/
│       ├── __init__.py
│       ├── plain_python.py
│       ├── poml_prompt.py
│       └── python_template.py
├── tests/
│   ├── test_content_components.py
│   ├── test_context_separation.py
│   ├── test_few_shot.py
│   ├── test_hello.py
│   ├── test_message_structure.py
│   ├── test_prompt_comparison.py
│   ├── test_roles.py
│   ├── test_technical_advisor.py
│   └── test_variables.py
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## Setup

```powershell
python -m venv .venv311
.\.venv311\Scripts\Activate.ps1
pip install -r requirements.txt
```

Copy `.env.example` to `.env` and fill in your `OPENAI_API_KEY` when
LLM calls are added in a later phase.

## Running Tests

```powershell
python -m pytest
```