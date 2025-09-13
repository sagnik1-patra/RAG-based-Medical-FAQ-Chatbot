import chromadb
from src.config import CHROMA_DIR, TOP_K

def get_collection():
    return chromadb.PersistentClient(path=CHROMA_DIR).get_collection("medical_faqs")

def retrieve(query: str, k=TOP_K):
    coll = get_collection()
    res = coll.query(query_texts=[query], n_results=k, include=["documents","metadatas","distances"])
    hits = []
    for i in range(len(res["documents"][0])):
        hits.append({
            "text": res["documents"][0][i],
            "meta": res["metadatas"][0][i],
            "score": float(res["distances"][0][i])
        })
    return hits
