from langchain_ollama.embeddings import OllamaEmbeddings

MODEL_NAME = "qwen3-embedding:latest"

def get_embeddings():
    return OllamaEmbeddings(model=MODEL_NAME)


