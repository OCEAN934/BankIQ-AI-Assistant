from app.services.llm_service import (
    generate_llm_response
)


def generate_document_suggestions(text):

    prompt = f"""
You are an enterprise document intelligence assistant.

Analyze the uploaded document and generate 4 intelligent
starter questions that a user would naturally ask after
reading this specific document.

STRICT RULES:

- Questions must come ONLY from topics explicitly present
  in the document.

- Do NOT invent generic banking, insurance, finance,
  policy, compliance or customer-service questions.

- Extract actual topics, clauses, definitions,
  coverage sections, exclusions, procedures,
  obligations, timelines, limits, conditions,
  approvals, penalties or exceptions discussed
  in the document.

- Every question must target a DIFFERENT section
  or concept from the document.

- Prefer questions that require reasoning,
  comparison, interpretation or explanation.

- Avoid yes/no questions whenever possible.

- Keep questions concise.

- Return ONLY the questions.

- One question per line.

- No numbering.

- No bullets.

DOCUMENT:

{text[:4000]}
"""

    response = generate_llm_response(
        prompt
    )

    suggestions = [

        line.strip("- ").strip()

        for line in response.split("\n")

        if line.strip()
    ]

    return suggestions[:4]