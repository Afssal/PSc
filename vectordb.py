import chromadb
from chromadb.utils.embedding_functions.ollama_embedding_function import (
    OllamaEmbeddingFunction
)


ollama_ef = OllamaEmbeddingFunction(
    url="http://localhost:11434",
    model_name="nomic-embed-text:latest"
)

client = chromadb.PersistentClient(path="DataBase")


collection = client.create_collection(name="economics",
                                      embedding_function=ollama_ef
                                      )







