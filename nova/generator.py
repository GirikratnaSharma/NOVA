import re
from llama_cpp import Llama, llama_log_set

llama_log_set(None, None)

# Disable internal logs

def initialize_conversation():
    return [
        {
            "role": "system",
            "content": "You are NOVA, a spaceflight assistant AI. Use the context below to answer the astronaut's question."
        }
    ]

class Generator:
    def __init__(self):
        self.generator = Llama.from_pretrained(
            repo_id="unsloth/Llama-3.2-3B-Instruct-GGUF",
            filename="Llama-3.2-3B-Instruct-Q3_K_M.gguf",
            n_ctx=16384
        )
        # self.generator = pipeline("text2text-generation", model="google/flan-t5-base")
        self.conversation = initialize_conversation()

    def generate_response(self, context, query):
        prompt = {"role": "user", "content": f"context: {context}\n\n{query}"}
        self.conversation.append(prompt)

        raw_output = self.generator.create_chat_completion(
            messages=self.conversation
        )["choices"][0]["message"]["content"].strip()

        response = {"role": "assistant", "content": raw_output}
        self.conversation.append(response)

        # Clean artifacts
        cleaned = raw_output.split("Question:")[0].strip()
        if re.search(r"\b\d+\.$", cleaned):
            cleaned = re.sub(r"\b\d+\.$", "", cleaned).strip()

        return raw_output