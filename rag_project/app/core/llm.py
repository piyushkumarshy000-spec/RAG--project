from groq import Groq
from app.config import settings

client = Groq(api_key=settings.GROQ_API_KEY)

def generate_answer(context, question):
    prompt = f"""
    You are a strict assistant.

    Rules:
    - Answer ONLY from context
    - If not found, say "Not available"
    - Be concise and structured

    Context:
    {context}

    Question:
    {question}
    """

    response = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[{"role": "user", "content": prompt}],
    temperature=0.2
)

    return response.choices[0].message.content