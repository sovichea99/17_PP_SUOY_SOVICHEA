from __future__ import annotations

from app.config import TOP_K
from app.generator import generate_answer
from app.retrieval import retrieve


def run_pipeline(question: str, top_k: int = TOP_K) -> dict:
    chunks = retrieve(question, top_k=top_k)
    answer = generate_answer(question, chunks)
    sources = sorted({chunk["source"] for chunk in chunks})

    return {
        "question": question,
        "answer": answer,
        "sources": sources,
        "chunks": chunks,
    }

# if __name__ == "__main__":
#     question = "how to reset the password?"

#     result = run_pipeline(question)
#     print(f"Question: {result['question']}")
#     print("\nAnswer:")
#     print(result["answer"])
#     print(f"\nSources: {', '.join(result['sources']) or 'none'}")
