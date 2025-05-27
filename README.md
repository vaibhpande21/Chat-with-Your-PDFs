# RAG-Powered PDF Chatbot

A lightweight, production-ready chatbot that uses **Retrieval-Augmented Generation (RAG)** to answer questions from any PDF document. Built with **LangChain**, **OpenAI**, **ChromaDB**, and **FastAPI**.

---

##  What It Does

1. Extracts text from PDF files
2. Splits and stores the chunks as vector embeddings (OpenAI)
3. Retrieves relevant chunks using a vector database (Chroma)
4. Uses OpenAI’s LLM to answer your questions contextually
5. Provides a blazing-fast API endpoint (`/ask`) for integration

