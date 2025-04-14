# nova/rag_pipeline.py
from nova.retriever import Retriever
from nova.generator import Generator

class RAGPipeline:
    def __init__(self):
        self.retriever = Retriever()
        self.generator = Generator()
        self.retriever.index_documents()

    def run(self, query):
        docs = self.retriever.retrieve(query)
        return self.generator.generate_response(docs[0], query)
