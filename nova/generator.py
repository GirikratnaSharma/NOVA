from transformers import pipeline
import re

class Generator:
    def __init__(self):
        self.generator = pipeline("text2text-generation", model="google/flan-t5-base")

    def generate_response(self, context, query):
        prompt = f"""You are NOVA, a spaceflight assistant AI. 
Use the context below to answer the astronaut's question.

Context: {context}

Question: {query}
"""
        result = self.generator(
            prompt,
            max_length=150,
            truncation=True
        )

        raw_output = result[0]['generated_text'].strip()

        # Remove weird artifacts like repeated prompts or broken steps
        cleaned = raw_output.split("Question:")[0].strip()

        # Remove hanging "number + dot" endings like "3."
        if re.search(r"\b\d+\.$", cleaned):
            cleaned = re.sub(r"\b\d+\.$", "", cleaned).strip()

        return cleaned
