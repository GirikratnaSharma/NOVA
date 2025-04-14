# nova/generator.py
from transformers import pipeline

class Generator:
    def __init__(self):
        self.generator = pipeline("text-generation", model="gpt2")

    def generate_response(self, context, query):
        prompt = f"Context: {context}\n\nQuestion: {query}\nAnswer:"
        result = self.generator(prompt, max_length=100, do_sample=True, truncation=True)

        return result[0]['generated_text'].split("Answer:")[-1].strip()
