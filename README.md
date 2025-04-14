# 🚀 NOVA — Neural Operator for Virtual Assistance

> An intelligent mission support system powered by Retrieval-Augmented Generation (RAG) and Transformer-based language models.

---

## 🌌 Project Overview

**NOVA** (Neural Operator for Virtual Assistance) is a next-gen software AI assistant designed to simulate decision-making and procedural support for spaceflight environments.

Built using modern NLP techniques — including transformer models from Hugging Face and document retrieval via FAISS — NOVA allows users to query space mission procedures, logs, and protocols in natural language.

Think of it as **HAL 9000** meets **ChatGPT**, minus the existential threat.

---

## 🧠 Features

- 🔍 **Retrieval-Augmented Generation (RAG)** pipeline
- 📚 Answers grounded in real mission documents (e.g., EVA checklists, system protocols)
- 🤖 Hugging Face Transformers integration
- 💬 Natural language query support for mission-critical situations
- 🧪 Simulated space ops use-cases (life support, system reboot, diagnostics)
- ⚡ Lightweight CLI interface *(GUI coming soon)*

---

## 📁 Folder Structure

nova/
├── data/                  # Mission documents (e.g., NASA PDFs, checklists)
├── embeddings/            # Vector index (FAISS or Chroma)
├── nova/                 
│   ├── assistant.py       # Main chat agent
│   ├── rag_pipeline.py    # Retriever + Generator integration
│   ├── retriever.py       # FAISS retriever logic
│   └── generator.py       # Language model handler
├── utils/                 # PDF/text parsers and helpers
├── app.py                 # CLI entry point
├── LICENSE                # MIT License
└── README.md              # Project readme


## 🚀 Getting Started

### 1. Clone the Repo
```bash
git clone https://github.com/GirikratnaSharma/NOVA.git
cd NOVA
```

### 2. Set Up Environment
```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### 3. Run the Assistant
```bash
python app.py
```

Then ask questions like:
```plaintext
> "How do I reboot the backup oxygen system?"
> "What’s the last known log on the CO2 levels?"
```

