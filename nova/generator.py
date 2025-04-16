import re
import contextlib
import os
import sys
from llama_cpp import Llama, llama_log_set

# Disable internal logs
llama_log_set(None, None)

@contextlib.contextmanager
def suppress_stdout():
    with open(os.devnull, "w") as devnull:
        old_stdout = sys.stdout
        old_stderr = sys.stderr
        try:
            sys.stdout = devnull
            sys.stderr = devnull
            yield
        finally:
            sys.stdout = old_stdout
            sys.stderr = old_stderr

def initialize_conversation():
    return [
        {
            "role": "system",
            "content": "You are NOVA, a spaceflight assistant AI. Use the context below to answer the astronaut's question."
        }
    ]

class Generator:
    def __init__(self):
        with suppress_stdout():
            self.generator = Llama.from_pretrained(
                repo_id="unsloth/Llama-3.2-3B-Instruct-GGUF",
                filename="Llama-3.2-3B-Instruct-Q3_K_M.gguf",
                n_ctx=16384
            )
        self.conversation = initialize_conversation()

    def generate_response(self, context, query):
        prompt = {"role": "user", "content": f"context: {context}\n\n{query}"}
        self.conversation.append(prompt)

        with suppress_stdout():
            raw_output = self.generator.create_chat_completion(
                messages=self.conversation
            )["choices"][0]["message"]["content"].strip()

        # Ensure there's a newline at the start
        formatted_output = "\n" + raw_output.strip()

        response = {"role": "assistant", "content": formatted_output}
        self.conversation.append(response)

        # Clean artifacts (optional still)
        cleaned = formatted_output.split("Question:")[0].strip()
        if re.search(r"\b\d+\.$", cleaned):
            cleaned = re.sub(r"\b\d+\.$", "", cleaned).strip()

        return formatted_output
