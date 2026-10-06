# 🧠 SmartNotes AI

SmartNotes AI is an AI-powered study assistant that helps students understand and interact with their PDF notes.

The application extracts text from uploaded PDF documents, processes the content, creates semantic embeddings, stores them in a vector database, and uses Retrieval-Augmented Generation (RAG) to answer questions based on the uploaded notes.

It also provides AI-powered text summarization to help students quickly understand lengthy study material.

---

## 📌 Problem Statement

Students often spend a lot of time reading lengthy PDF notes and searching for specific information.

Traditional PDF readers only allow users to search for exact words or phrases. They cannot understand the meaning of a question and retrieve the most relevant information from the document.

SmartNotes AI solves this problem by allowing students to:

- Upload PDF notes
- Extract and process their content
- Generate AI-based summaries
- Ask questions about their notes
- Get answers based only on the relevant content from the uploaded PDF

---

## 🎯 Objectives

The main objectives of SmartNotes AI are:

- To simplify studying from lengthy PDF documents
- To automatically summarize study material
- To allow students to ask questions in natural language
- To retrieve relevant information using semantic similarity
- To use RAG to generate context-aware answers
- To provide an easy-to-use student-friendly interface

---

## ✨ Features

### 📄 PDF Upload
Users can upload PDF study materials through the Streamlit interface.

### 📝 Text Extraction
Text is extracted from PDF files using PyPDF.

### ✂️ Text Cleaning & Chunking
The extracted text is cleaned and divided into smaller chunks for efficient processing.

### 🔢 Text Embeddings
Each text chunk is converted into a numerical vector using the Sentence Transformer model:

`all-MiniLM-L6-v2`

### 🗄️ Vector Database
The embeddings are stored in ChromaDB for efficient similarity search.

### 🔍 Semantic Search
When a user asks a question, the question is converted into an embedding and compared with stored document embeddings.

The most relevant chunks are retrieved.

### 🤖 RAG-based Question Answering
The retrieved document chunks are provided as context to the Llama 3.2 language model.

The model generates an answer based on the retrieved information.

### 📑 AI Summarization
The application uses a pretrained Transformer model to generate a concise summary of the document content.

### 💻 Interactive UI
The complete application is built using Streamlit.

---

## 🔄 System Workflow

```text
                 ┌─────────────────┐
                 │   Upload PDF    │
                 └────────┬────────┘
                          ↓
                 ┌─────────────────┐
                 │  Extract Text   │
                 │     PyPDF       │
                 └────────┬────────┘
                          ↓
                 ┌─────────────────┐
                 │  Clean Text     │
                 └────────┬────────┘
                          ↓
                 ┌─────────────────┐
                 │  Create Chunks  │
                 └────────┬────────┘
                          ↓
                 ┌─────────────────┐
                 │   Embeddings    │
                 │ MiniLM Model    │
                 └────────┬────────┘
                          ↓
                 ┌─────────────────┐
                 │    ChromaDB     │
                 │ Vector Database │
                 └────────┬────────┘
                          ↓
             ┌─────────────────────────┐
             │      User Question      │
             └────────────┬────────────┘
                          ↓
             ┌─────────────────────────┐
             │ Question Embedding      │
             └────────────┬────────────┘
                          ↓
             ┌─────────────────────────┐
             │   Similarity Search     │
             └────────────┬────────────┘
                          ↓
             ┌─────────────────────────┐
             │ Relevant Text Chunks    │
             └────────────┬────────────┘
                          ↓
             ┌─────────────────────────┐
             │      Llama 3.2          │
             │       + Context         │
             └────────────┬────────────┘
                          ↓
                 ┌─────────────────┐
                 │   AI Answer     │
                 └─────────────────┘

                 SmartNotesAI/


📁 Project Structure

│
├── app.py
├── README.md
├── requirements.txt
├── .gitignore
│
├── utils/
│   ├── __init__.py
│   ├── pdf_processor.py
│   ├── text_processor.py
│   ├── summarizer.py
│   ├── embeddings.py
│   └── rag.py
│
├
│
├── models/
│
├── assets/
│   └── images/
│
└

    📦 Requirements
The main Python packages used in the project are:
streamlit>=1.40
transformers>=4.40,<5
torch>=2.1
pypdf>=4.0
sentence-transformers
chromadb
ollama