import re
import pandas as pd

def load_faqs(path: str) -> pd.DataFrame:
    if path.endswith(".csv"):
        df = pd.read_csv(path)
    elif path.endswith(".json"):
        df = pd.read_json(path)
    else:
        raise ValueError("Dataset must be CSV or JSON")
    df = df.rename(columns={c: c.lower() for c in df.columns})
    assert "question" in df.columns and "answer" in df.columns, "Need 'question' and 'answer' cols"
    if "source" not in df.columns:
        df["source"] = "medical_faq"
    return df

def clean_text(s: str) -> str:
    return re.sub(r"\s+", " ", str(s)).strip()

def chunk_text(text: str, chunk_chars=800, overlap=120):
    text = clean_text(text)
    if len(text) <= chunk_chars:
        return [text]
    chunks, start = [], 0
    while start < len(text):
        end = min(len(text), start+chunk_chars)
        chunks.append(text[start:end])
        start = end - overlap
        if start >= len(text):
            break
    return chunks

def rows_to_documents(df: pd.DataFrame):
    docs = []
    for i, row in df.iterrows():
        base = f"Q: {clean_text(row['question'])}\nA: {clean_text(row['answer'])}"
        for j, chunk in enumerate(chunk_text(base)):
            docs.append({
                "id": f"doc_{i}_{j}",
                "text": chunk,
                "meta": {"row_id": int(i), "source": row.get("source","medical_faq")}
            })
    return docs
