from sentence_transformers import SentenceTransformer
import faiss
import os
import pickle
from utils.parser import load_documents_from_folder

class Retriever:
    def __init__(self, docs_dir="data/", index_path="embeddings/faiss.index"):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.docs_dir = docs_dir
        self.index_path = index_path
        self.index = faiss.IndexFlatL2(384)
        self.text_chunks = []

        if os.path.exists(self.index_path):
            print("🔁 Loading existing FAISS index...")
            self.load_index()
        else:
            print("🧠 Indexing documents for the first time...")
            self.index_documents()
            self.save_index()

    def index_documents(self):
        self.text_chunks = load_documents_from_folder(self.docs_dir)
        embeddings = self.model.encode(self.text_chunks)
        self.index.add(embeddings)

    def save_index(self):
        faiss.write_index(self.index, self.index_path)
        with open("embeddings/text_chunks.pkl", "wb") as f:
            pickle.dump(self.text_chunks, f)

    def load_index(self):
        self.index = faiss.read_index(self.index_path)
        with open("embeddings/text_chunks.pkl", "rb") as f:
            self.text_chunks = pickle.load(f)

    def retrieve(self, query, top_k=1):
        query_vec = self.model.encode([query])
        _, indices = self.index.search(query_vec, top_k)
        return [self.text_chunks[i] for i in indices[0]]
