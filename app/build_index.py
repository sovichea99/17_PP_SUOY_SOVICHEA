from app.chunking import chunk_text
from app.ingestion import load_documents
from app.config import CHUNK_OVERLAP, CHUNK_SIZE, DATA_DIR
from app.embeddings import embed_texts
from app.vector_store import add_chunks 

def build_index():
    ids, texts, metadatas = [], [], []
    for filename, full_text in load_documents():
        for i, chunk in enumerate(chunk_text(full_text, chunk_size=CHUNK_SIZE, overlap=CHUNK_OVERLAP)):
            ids.append(f"{filename}::{i}")
            texts.append(chunk)
            metadatas.append({"source": filename, "chunk_index": i})
    embeddings = embed_texts(texts)
    add_chunks(ids, texts, embeddings, metadatas)
    return len(texts)


if __name__ == "__main__":
    print(f"Indexed {build_index()} chunks.")