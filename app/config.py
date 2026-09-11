

EMBED_MODEL = "nomic-embed-text"
GEN_MODEL = "llama3.2:3b"

# --- Storage ---
DATA_DIR = "data"                 
CHROMA_DB_DIR = "chroma_db"  
COLLECTION_NAME = "documents"

# --- Chunking ---
CHUNK_SIZE = 800  
CHUNK_OVERLAP = 120

# --- Retrieval ---
TOP_K = 3

# --- Generation ---
SYSTEM_PROMPT = (
    "You are a helpful, concise assistant. Answer the user's question using ONLY the provided context.\n"
    "CRITICAL RULES:\n"
    "1. Summarize the steps briefly. DO NOT copy-paste the context word-for-word.\n"
    "2. Merge overlapping information from different chunks. DO NOT repeat the same steps.\n"
    "3. Keep the answer as short and direct as possible.\n"
    "4. If the answer is not in the context, say exactly: \"I don't have enough information in the documents to answer that.\"\n"
    "5. Always cite the source file name(s) at the end."
)
