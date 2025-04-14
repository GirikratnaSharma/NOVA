import os
import fitz  # PyMuPDF
import re

def load_txt_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()

def load_pdf_file(filepath):
    text = ""
    with fitz.open(filepath) as doc:
        for page in doc:
            text += page.get_text()
    return text

def chunk_text(text, chunk_size=5):
    # Basic sentence splitting using punctuation
    sentences = re.split(r'(?<=[.!?])\s+', text.strip())
    chunks = [" ".join(sentences[i:i+chunk_size]) for i in range(0, len(sentences), chunk_size)]
    return chunks

def load_documents_from_folder(folder_path):
    all_chunks = []
    for filename in os.listdir(folder_path):
        full_path = os.path.join(folder_path, filename)

        if filename.endswith(".txt"):
            text = load_txt_file(full_path)
        elif filename.endswith(".pdf"):
            text = load_pdf_file(full_path)
        else:
            continue

        chunks = chunk_text(text)
        all_chunks.extend(chunks)

    return all_chunks
