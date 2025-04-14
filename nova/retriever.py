# nova/retriever.py
from sentence_transformers import SentenceTransformer
import faiss
import os

class Retriever:
    def __init__(self, docs_dir="data/"):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.docs_dir = docs_dir
        self.index = faiss.IndexFlatL2(384)
        self.text_chunks = []
        self.embeddings = []

    def load_documents(self):
        for filename in os.listdir(self.docs_dir):
            with open(os.path.join(self.docs_dir, filename), "r", encoding="utf-8") as f:
                text = f.read()
                self.text_chunks.append(text)

    def index_documents(self):
        self.load_documents()
        self.embeddings = self.model.encode(self.text_chunks)
        self.index.add(self.embeddings)

    def retrieve(self, query, top_k=1):
        query_vec = self.model.encode([query])
        _, indices = self.index.search(query_vec, top_k)
        return [self.text_chunks[i] for i in indices[0]]
