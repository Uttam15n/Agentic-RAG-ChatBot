# 📚 Agentic RAG Chatbot

<p align="center">

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![LangChain](https://img.shields.io/badge/LangChain-Agentic-green)
![LangGraph](https://img.shields.io/badge/LangGraph-Stateful-orange)
![ChromaDB](https://img.shields.io/badge/VectorDB-ChromaDB-purple)
![Gemini](https://img.shields.io/badge/Embeddings-Google_Gemini-red)
![Groq](https://img.shields.io/badge/LLM-Groq-black)
![Streamlit](https://img.shields.io/badge/UI-Streamlit-ff4b4b)

</p>

---

# 📖 Overview

Agentic RAG Chatbot is an intelligent document question-answering system that enables users to upload PDF documents and interact with them using natural language.

Unlike traditional chatbots, this application uses **Retrieval-Augmented Generation (RAG)** along with an **Agentic workflow powered by LangGraph** to retrieve only the most relevant document chunks before generating responses. This significantly reduces unnecessary context passed to the LLM, resulting in faster, more accurate, and cost-efficient answers.

The project integrates **Google Gemini Embeddings**, **ChromaDB**, **Groq LLMs**, **LangChain**, and **Streamlit** to provide a conversational experience with persistent memory.

---

# ✨ Features

- 📄 Upload one or multiple PDF documents
- 🔍 Semantic document retrieval using vector embeddings
- 🧠 Conversational memory for follow-up questions
- ⚡ High-speed inference using Groq LLM
- 📚 ChromaDB vector storage
- 🤖 LangGraph-powered agent workflow
- 🎯 Context-aware responses
- 💬 Natural language question answering
- 🖥️ Interactive Streamlit interface

---

# 🏗️ System Architecture

```mermaid
flowchart LR

A[User Uploads PDF]
B[Document Loader]
C[Text Splitter]
D[Gemini Embeddings]
E[ChromaDB Vector Store]
F[Retriever]
G[LangGraph Agent]
H[Groq LLM]
I[Final Response]

A --> B
B --> C
C --> D
D --> E
E --> F
F --> G
G --> H
H --> I
```

---

# 🔄 Workflow

```mermaid
sequenceDiagram

participant User
participant Streamlit
participant Retriever
participant ChromaDB
participant Groq

User->>Streamlit: Upload PDF
Streamlit->>Retriever: Process Document
Retriever->>ChromaDB: Store Embeddings

User->>Streamlit: Ask Question

Streamlit->>Retriever: Retrieve Relevant Chunks

Retriever->>ChromaDB: Similarity Search

ChromaDB-->>Retriever: Top Relevant Context

Retriever->>Groq: Prompt + Context

Groq-->>Streamlit: AI Response

Streamlit-->>User: Display Answer
```

---

# 🛠 Tech Stack

| Category | Technologies |
|----------|--------------|
| Language | Python |
| Framework | LangChain |
| Agent Framework | LangGraph |
| LLM | Groq |
| Embeddings | Google Gemini Embeddings |
| Vector Database | ChromaDB |
| UI | Streamlit |
| Environment | Python Virtual Environment |

---


# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/agentic-rag-chatbot.git

cd agentic-rag-chatbot
```

Create virtual environment

```bash
python -m venv venv
```

Activate

Windows

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env`

```text
GOOGLE_API_KEY=

GROQ_API_KEY=
```

---

# ▶️ Run Application

```bash
streamlit run app.py
```

---

# 💡 How It Works

### Step 1

Upload one or multiple PDF documents.

↓

### Step 2

Documents are split into smaller semantic chunks.

↓

### Step 3

Each chunk is converted into embeddings using Google Gemini Embeddings.

↓

### Step 4

Embeddings are stored inside ChromaDB.

↓

### Step 5

When a user asks a question, similarity search retrieves the most relevant chunks.

↓

### Step 6

The retrieved context is passed to the Groq LLM.

↓

### Step 7

The chatbot generates an accurate response grounded in the uploaded documents.

---




## Upload PDF

<img width="1588" height="868" alt="Screenshot 2026-08-01 111423" src="https://github.com/user-attachments/assets/43eef14f-6e48-4c8f-bde9-37437b8ceff1" />

---

## Chat Interface

<img width="1655" height="927" alt="Screenshot 2026-08-01 111521" src="https://github.com/user-attachments/assets/76cc55b8-ebc8-48a0-9ffc-a94c398ece8a" />

---

# 🚀 Future Improvements

- Multi-document collections
- Hybrid Search (BM25 + Vector Search)
- Document summarization
- Citation-aware responses
- Authentication
- Docker support
- Cloud deployment
- Streaming responses
- Multi-user conversations

---

# 📈 Learning Outcomes

This project strengthened my understanding of:

- Retrieval-Augmented Generation (RAG)
- LangChain pipelines
- LangGraph stateful workflows
- Vector databases
- Embedding models
- Prompt engineering
- Conversational memory
- LLM orchestration
- Semantic search

---

# 🤝 Contributing

Contributions are welcome.

If you would like to improve the project:

1. Fork the repository

2. Create a feature branch

3. Commit your changes

4. Open a Pull Request

---

# 📄 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Uttam N**

Final Year Computer Science (Cyber Security)

Passionate about

- Software Engineering
- Artificial Intelligence
- Generative AI
- Agentic AI Systems
- Large Language Models

LinkedIn: *Add Your Profile*

GitHub: *Add Your Profile*

---

## ⭐ If you found this project useful, consider giving it a star!
