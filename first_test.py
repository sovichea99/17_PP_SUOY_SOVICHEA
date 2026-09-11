import ollama

# test generation model
resp = ollama.chat(model="llama3.2:3b", messages=[{"role": "user", "content": "Say hello in 5 words."}])
print("CHAT:", resp.message.content)

# test embedding model
emb = ollama.embed(model="nomic-embed-text", input=["hello world"])
print("EMBED length:", len(emb.embeddings[0]))