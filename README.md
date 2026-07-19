# 🤖 SQL Mentor AI

An interactive, AI-powered SQL tutoring chatbot built using a **Retrieval-Augmented Generation (RAG)** architecture. The application leverages LangChain, Groq (Llama 3.3), and Streamlit to answer user SQL questions accurately by referencing authoritative local documentation.

---

## 🚀 Features

* **Context-Aware Assistance:** Utilizes semantic search via a local FAISS vector store to retrieve highly relevant context from SQL technical documentation.
* **Blazing Fast Responses:** Powered by the `llama-3.3-70b-versatile` model hosted on Groq for sub-second, intelligent inference.
* **Streamlit Chat UI:** An intuitive, conversational interface mimicking modern chat systems with persistent session state management.
* **Efficient Ingestion:** Modular script to chunk, embed, and store reference manuals locally using Hugging Face embeddings.

---

## 📂 Project Architecture

The repository is structured neatly to isolate data ingestion from the frontend interface:

```text
├── app.py               # Main Streamlit application and chat UI
├── vector_db.py         # Data ingestion script (PDF parsing & FAISS index creation)
├── vectorstore/         # Pre-built FAISS vector database indices
├── requirements.txt     # Python package dependencies
├── .env.example         # Template for required environment variables
└── .gitignore           # Safeguard file preventing key and environment leaks
