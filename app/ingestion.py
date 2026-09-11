import os

from app.config import DATA_DIR

def load_documents(data_dir: str = DATA_DIR) -> list[tuple[str, str]]:
    if data_dir is None:
        data_dir = DATA_DIR

    documents = []
    for filename in sorted(os.listdir(data_dir)):
        path = os.path.join(data_dir, filename)
        if not os.path.isfile(path):
            continue
        if filename.lower().endswith((".txt", ".md")):
            with open(path, "r", encoding="utf-8") as f:
                text = f.read()
            if text.strip():
                documents.append((filename, text))
    return documents


# if __name__ == "__main__":
#     documents = load_documents()
#     print(f"Loaded {len(documents)} documents from '{DATA_DIR}/'.")
#     for filename, text in documents:
#         print(f"- {filename}: {len(text)} characters")