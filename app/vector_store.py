import logging

import chromadb
from chromadb.config import Settings

from app.config import CHROMA_DB_DIR, COLLECTION_NAME, TOP_K

_telemetry_logger = logging.getLogger("chromadb.telemetry.product.posthog")
_telemetry_logger.setLevel(logging.CRITICAL)
_telemetry_logger.propagate = False

_settings = Settings(anonymized_telemetry=False)

def get_collection():
    client = chromadb.PersistentClient(path=CHROMA_DB_DIR, settings=_settings)
    return client.get_or_create_collection(name=COLLECTION_NAME)

def add_chunks(ids, texts, embeddings, metadatas):
    collection = get_collection()
    existing_ids = collection.get()["ids"]
    if existing_ids:
        collection.delete(ids=existing_ids)
    collection.add(ids=ids, documents=texts, embeddings=embeddings, metadatas=metadatas)

def search(query_embedding, top_k=TOP_K):
    collection = get_collection()
    return collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k,
        include=["documents", "metadatas", "distances"],
    )