import argparse
from src.retriever import retrieve
from src.generator import answer

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("question", type=str)
    args = ap.parse_args()
    hits = retrieve(args.question)
    print("=== Retrieved ===")
    for h in hits:
        print(f"- {h['text']} ({h['meta']})")
    print("\n=== Answer ===")
    print(answer(args.question, hits))
