from nova.retriever import Retriever
from nova.generator import Generator

class RAGPipeline:
    def __init__(self):
        self.retriever = Retriever()
        self.generator = Generator()
        self.retriever.index_documents()

    def run(self, query):
        docs = self.retriever.retrieve(query, top_k=2)
        context = "\n".join(docs)

        # Fallback if no useful docs retrieved
        if "couldn’t find anything relevant" in docs[0]:
            print("No match found in documents. Falling back to general generation.\n")
            return self.generator.generate_response("", query)

        return self.generator.generate_response(context, query)
