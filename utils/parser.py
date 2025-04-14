# utils/parser.py

import os
import fitz  # PyMuPDF

def load_txt_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()

def load_pdf_file(filepath):
    doc = fitz.open(filepath)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def load_documents_from_folder(folder_path):
    documents = []
    for filename in os.listdir(folder_path):
        full_path = os.path.join(folder_path, filename)
        if filename.endswith(".txt"):
            documents.append(load_txt_file(full_path))
        elif filename.endswith(".pdf"):
            documents.append(load_pdf_file(full_path))
    return documents
