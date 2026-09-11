from typing import List

import ollama

from app.config import EMBED_MODEL


def embed_texts(texts: List[str]) -> List[List[float]]:
    if not texts:
        return []
    response = ollama.embed(model=EMBED_MODEL, input=texts)
    return list(response.embeddings)


def embed_query(text: str) -> List[float]:
    return embed_texts([text])[0]
