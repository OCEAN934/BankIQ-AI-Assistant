from groq import Groq

from app.core.config import settings


client = Groq(
    api_key=settings.GROQ_API_KEY
)


SYSTEM_PROMPT = """
You are BankIQ, an expert banking and policy assistant.

RULES:
- Answer ONLY using the provided context.
- Do NOT hallucinate or invent facts.
- If partial information exists, provide the available information clearly.
- Only state that information is insufficient if the context is completely unrelated.
- Give informative and professional answers.
- Include important conditions, implications, or requirements when relevant.
- Use concise but meaningful explanations.
"""


def generate_llm_response(prompt):

    completion = client.chat.completions.create(
        model=settings.MODEL_NAME,
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2,
        max_tokens=700
    )

    return completion.choices[0].message.content