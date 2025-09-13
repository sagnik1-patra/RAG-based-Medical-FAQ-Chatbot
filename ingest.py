import chromadb
from openai import OpenAI
from src.config import OPENAI_API_KEY, EMBED_MODEL, CHROMA_DIR
from src.utils import load_faqs, rows_to_documents

def embed_texts(client, texts):
    resp = client.embeddings.create(model=EMBED_MODEL, input=texts)
    return [d.embedding for d in resp.data]

def main():
    df = load_faqs("data/train.csv")
    docs = rows_to_documents(df)

    client = OpenAI(api_key=OPENAI_API_KEY)
    texts = [d["text"] for d in docs]
    vectors = embed_texts(client, texts)

    c = chromadb.PersistentClient(path=CHROMA_DIR)
    try: c.delete_collection("medical_faqs")
    except: pass
    coll = c.create_collection("medical_faqs")

    coll.add(
        ids=[d["id"] for d in docs],
        embeddings=vectors,
        documents=texts,
        metadatas=[d["meta"] for d in docs]
    )
    print(f"[OK] Ingested {len(docs)} chunks")

if __name__ == "__main__":
    main()
