# 🤖 RAG Assistant (FastAPI + FAISS + Groq)

A production-style Retrieval-Augmented Generation (RAG) system with:

* 🔍 Semantic Search (FAISS)
* 🧠 Reranking (Cross Encoder)
* 🤖 LLM (Groq)
* 📄 PDF & TXT Upload
* 💬 Chat UI

---

## 🚀 Features

* Ask questions from your documents
* Upload PDF/TXT files dynamically
* Accurate answers using reranking
* Source citations included
* Clean web UI

---

## 📦 Installation

### 1. Clone repo

```bash
git clone https://github.com/your-username/rag-project.git
cd rag-project
```

---

### 2. Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate  # Mac/Linux
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Add API key

Create `.env` file:

```env
GROQ_API_KEY=your_api_key_here
```

---

## ▶️ Run the Project

```bash
uvicorn app.main:app --reload
```

---

## 🌐 Open UI

```
http://127.0.0.1:8000/
```

---

## 📄 Upload Files

* Supports `.pdf` and `.txt`
* Upload from UI
* Ask questions instantly

---

## 🧠 Tech Stack

* FastAPI
* FAISS
* Sentence Transformers
* Groq LLM
* HTML + JS

---

## ⚠️ Notes

* Python 3.10 or 3.11 recommended
* Some PDFs (scanned) may not extract text

---

## 🚀 Future Improvements

* Chat memory
* Highlight answers
* Cloud deployment
