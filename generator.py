from openai import OpenAI
from src.config import OPENAI_API_KEY, CHAT_MODEL

SYSTEM_PROMPT = """You are a helpful medical assistant.
Answer using only the given context.
If unsure, say "I don't know based on the provided info."
Add [source] citations when possible.
"""

def build_context(hits):
    return "\n\n".join([f"[{h['meta'].get('source','faq')}] {h['text']}" for h in hits])

def answer(query, hits):
    client = OpenAI(api_key=OPENAI_API_KEY)
    ctx = build_context(hits)
    user = f"Q: {query}\n\nContext:\n{ctx}"
    resp = client.chat.completions.create(
        model=CHAT_MODEL,
        temperature=0.2,
        messages=[
            {"role":"system","content":SYSTEM_PROMPT},
            {"role":"user","content":user}
        ]
    )
    return resp.choices[0].message.content.strip()
