import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
EMBED_MODEL    = os.getenv("EMBED_MODEL", "text-embedding-3-small")
CHAT_MODEL     = os.getenv("CHAT_MODEL", "gpt-4o-mini")
CHROMA_DIR     = os.getenv("CHROMA_DIR", "./chroma_db")
TOP_K          = int(os.getenv("TOP_K", "4"))
