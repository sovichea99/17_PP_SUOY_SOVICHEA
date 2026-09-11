# RAG Fundamentals — Baseline Chat with Documents

A simple local **Naive RAG (Retrieval-Augmented Generation)** application that answers questions using a small set of local text documents.

## RAG Pipeline

```text
Documents (.txt)
      ↓
Ingestion
      ↓
Chunking
      ↓
Embeddings (Ollama)
      ↓
ChromaDB
      ↓
Retrieval (top-k)
      ↓
Generation (Ollama)
      ↓
Grounded Answer
```

The project implements the five main RAG stages: **ingestion, chunking, embedding, retrieval, and generation**.

## Models and Tools

- **Generation model:** `llama3.2:3b`
- **Embedding model:** `nomic-embed-text`
- **Vector database:** ChromaDB (persistent mode)
- **Python dependency manager:** Poetry
- **LLM runtime:** Ollama

## Documents

The `data/` folder contains 5 text documents:

1. Setting Up a Mobile Device for Company Email
2. Resetting a Forgotten PIN
3. Configuring VPN Access for Remote Workers
4. Setting Up a Conference Call on Cisco Webex
5. Setting Up a Secure Wireless Network

## Prerequisites

Make sure Ollama is installed and running, then pull both models:

```bash
ollama pull llama3.2:3b
ollama pull nomic-embed-text
```

Check that they are available:

```bash
ollama list
```

Install the Python dependencies:

```bash
poetry install
```

## Run the App

### 1. Build the vector index

This loads the documents, splits them into chunks, creates embeddings, and stores the vectors in ChromaDB.

```bash
poetry run python -m app.build_index
```

You should see a message showing how many chunks were indexed.

### 2. Run the terminal chat

```bash
poetry run python -m app.main
```

Then type a question, for example:

```text
Ask a question: How do I reset my forgotten PIN?
```

Type `exit or quit` to quit.

## Chunking Strategy

The app uses a simple **fixed-size character chunking strategy**:

- Chunk size: **800 characters**
- Chunk overlap: **120 characters**

The overlap keeps some context from the previous chunk when a document is split. This is a simple baseline strategy suitable for the Naive RAG.

## Retrieval

The question is converted into an embedding using `nomic-embed-text`. ChromaDB searches for the most similar document chunks. The default is **top-k = 3**.

## Generation

The retrieved chunks and the user's question are sent to `llama3.2:3b`. The system prompt instructs the model to answer using only the retrieved context and to say when the documents do not contain enough information.

## Vector Store Check

Before using the chat application, you can test retrieval directly:

```bash
poetry run python demo_vector_check.py
```

This embeds a test question, retrieves the top 3 chunks, and prints their contents and distance scores.


## Project Structure

```text
app/
├── config.py          # models, chunking, retrieval, system prompt
├── ingestion.py       # loads .txt/.md documents
├── chunking.py        # splits documents into chunks
├── embeddings.py      # creates embeddings with Ollama
├── vector_store.py    # persistent ChromaDB storage/search
├── build_index.py     # offline ingestion → chunking → embedding → storage
├── retrieval.py       # retrieves relevant chunks
├── generator.py       # builds prompt and calls local LLM
├── pipeline.py        # connects retrieval and generation
└── main.py            # terminal chat loop

data/                  # 5 source documents
chroma_db/              # persistent vector database

demo_vector_check.py   # standalone retrieval check
Homework_Report       # Test-log and Reflection
README.md               # project documentation
```