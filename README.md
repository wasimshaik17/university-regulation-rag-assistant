# 🎓 University Regulation RAG Assistant

A Retrieval-Augmented Generation (RAG) based application that allows users to ask questions from university regulation PDFs and get accurate, context-based answers.

---

## 🚀 Features

- 📄 Load multiple PDF documents
- 🔍 Semantic search using vector embeddings
- 🤖 Local LLM (Ollama - FREE, no API cost)
- ⚡ Fast retrieval using FAISS
- 🧠 Context-aware answers (no hallucination)
- 📌 Source reference (page number, file)

---

## 🏗️ Project Architecture

User Query → Retriever → Relevant Chunks → LLM → Final Answer

- **Loader** → Reads PDF files
- **Splitter** → Breaks into chunks
- **Embeddings** → Converts text → vectors
- **Vector DB (FAISS)** → Stores embeddings
- **Retriever** → Finds relevant chunks
- **LLM (Ollama)** → Generates answer

---

## 🛠️ Tech Stack

- Python
- Streamlit (UI)
- LangChain
- FAISS (Vector Database)
- Ollama (Local LLM & Embeddings)
- PyPDFLoader

---

## 📦 Installation

### 1. Clone the Repository
```bash
git clone <your-repo-url>
cd university-rag
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 🤖 Setup Ollama (FREE LLM)

### Install Ollama:
https://ollama.com/download

### Pull Models:
```bash
ollama pull llama3
ollama pull nomic-embed-text
```

---

## ▶️ Run the Project

### Start Ollama
```bash
ollama serve
```

### Run Streamlit App
```bash
streamlit run app.py
```

Open in browser:
```
http://localhost:8501
```

---

## 📂 Data Setup

Place your PDF files inside:

```
data/
```

Example:
```
data/regulations.pdf
data/university_rules.pdf
```

---

## 💡 Example Questions

### 🎓 Academic Rules
- What is the minimum attendance required?
- How is CGPA calculated?

### 📊 Exams
- What is the grading system?
- What are supplementary exam rules?

### ⚖️ Policies
- What is the malpractice policy?
- What are revaluation rules?

---

## 📸 Output

- ✅ Accurate answer from PDF
- 📄 Shows source (page number + file)
- ❌ No hallucination (answers only from documents)

---

## ⚠️ Limitations

- Works only on provided PDFs
- Cannot answer general knowledge questions
- Depends on quality of documents

---

## 🚀 Future Improvements

- Chat history (like ChatGPT)
- Highlight answers from PDF
- Upload PDFs via UI
- Better UI/UX
- Multi-language support

---

## 🎯 Use Case

- University students
- Academic assistants
- Regulation search systems
- Knowledge base Q&A

---

## 🧑‍💻 Author

Wasim Rahamatulla Shaik  
B.Tech AI & ML (2027)

---

## ⭐ Project Highlights

- 100% FREE (no API cost)
- Uses local LLM (privacy-safe)
- Real-world RAG implementation
- Interview-ready project

---

## 📜 License

This project is for educational purposes.