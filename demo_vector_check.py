from app.embeddings import embed_query
from app.vector_store import get_collection


def main():
    question = "How do I enable VPN on a remote employee device?"
    query_embedding = embed_query(question)

    collection = get_collection()
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=3,
        include=["documents", "metadatas", "distances"],
    )

    print(f"Question: {question}\n")
    for idx, (doc, meta, dist) in enumerate(zip(results["documents"][0], results["metadatas"][0], results["distances"][0]), start=1):
        print(f"Result {idx}:")
        print(f"  Source: {meta.get('source', 'unknown')}")
        print(f"  Chunk: {meta.get('chunk_index', -1)}")
        print(f"  Distance: {dist:.4f}")
        print(f"  Preview: {doc[:200].replace(chr(10), ' ')}")
        print("-" * 80)


if __name__ == "__main__":
    main()
