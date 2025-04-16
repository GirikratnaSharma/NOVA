from nova.rag_pipeline import RAGPipeline

rag = RAGPipeline()

def chat_with_nova(prompt):
    return rag.run(prompt)