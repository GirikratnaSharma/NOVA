# nova/generator.py
from transformers import pipeline

class Generator:
    def __init__(self):
        self.generator = pipeline("text-generation", model="gpt2")

    def generate_response(self, context, query):
        prompt = f"Context: {context}\n\nQuestion: {query}\nAnswer:"
        result = self.generator(
            prompt,
            max_length=200,  # 🔥 Increase token budget
            do_sample=True,
            top_k=50,
            top_p=0.92,
            temperature=0.7,
            truncation=True,
            pad_token_id=50256  # GPT-2 end-of-sequence token
        )

        # Extract clean answer
        generated = result[0]['generated_text']
        answer = generated.split("Answer:")[-1].strip()

        # Optional: prevent overflow into hallucinated follow-ups
        cleaned = answer.split("Question:")[0].strip()

        return cleaned
