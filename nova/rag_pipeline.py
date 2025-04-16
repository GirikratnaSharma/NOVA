from nova.retriever import Retriever
from nova.generator import Generator

class RAGPipeline:
    def __init__(self):
        self.retriever = Retriever()
        self.generator = Generator()
        self.retriever.index_documents()

    def run(self, query):
        docs = self.retriever.retrieve(query, top_k=5)

        if docs and isinstance(docs, list) and "couldn’t find anything relevant" in docs[0]:
            print("No match found in documents. Falling back to general generation.")
            return self.generator.generate_response("", query)

        context = "\n".join(docs)
        return self.generator.generate_response(context, query)