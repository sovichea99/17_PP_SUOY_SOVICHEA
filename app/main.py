from app.pipeline import run_pipeline

def run_cli():
    print("Type 'exit' to quit.")
    while True:
        question = input("Ask a question: ").strip()

        if not question:
            print("Please enter a question.")
            continue

        if question.lower() == "exit" or question.lower() == "quit":
            print("Goodbye!")
            break

        result = run_pipeline(question)
        print("\n--- Retrieved Sources ---")
        for i, chunk in enumerate(result["chunks"]):
            snippet = chunk["text"].replace("\n", " ")[:80]
            print(f"  Chunk {i+1} [{chunk['source']}]: \"{snippet}...\"")

        print("\n--- Final Answer ---")
        print(result["answer"])
        print("-" * 30 + "\n")


if __name__ == "__main__":
    run_cli()
