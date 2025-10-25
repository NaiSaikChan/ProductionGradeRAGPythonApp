from llama_index.readers.file import PDFReader
from llama_index.core.node_parser import SentenceSplitter
from dotenv import load_dotenv
import os
from ollama import Client as OllamaClient

load_dotenv()

# Using Ollama exclusively
client = OllamaClient(host=os.getenv("OLLAMA_HOST", "http://localhost:11434"))
EMBED_MODEL = "nomic-embed-text"
EMBED_DIM = 768

splitter = SentenceSplitter(chunk_size=1000, chunk_overlap=200)

def load_and_chunk_pdf(path: str):
    docs = PDFReader().load_data(file=path)
    texts = [d.text for d in docs if getattr(d, "text", None)]
    chunks = []
    for t in texts:
        chunks.extend(splitter.split_text(t))
    return chunks


def embed_texts(texts: list[str]) -> list[list[float]]:
    """Generate embeddings using Ollama's nomic-embed-text model"""
    embeddings = []
    for text in texts:
        response = client.embeddings(model=EMBED_MODEL, prompt=text)
        embeddings.append(response['embedding'])
    return embeddings