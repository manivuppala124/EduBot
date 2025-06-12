# 🤖 EduBot – Personalized AI Learning Assistant using Gemini 1.5 + LangChain

**EduBot** is a smart AI-powered learning assistant that dynamically generates quizzes and personalized summaries from PDF content or user input. It leverages **Gemini 1.5**, **LangChain**, and **RAG (Retrieval-Augmented Generation)** with vector databases to provide a cutting-edge learning experience.

This is one of my 2–3 well-documented, production-ready AI projects with full working code.  
✅ GitHub link is included in my resume.

---

## 🔥 Why EduBot? (Project Description – 200–300 words)

EduBot is built to transform how students study. Traditional learning tools lack interactivity, but EduBot solves this by generating MCQs, summaries, and explanations using AI in real-time. The app accepts PDFs or topic prompts and then performs chunking, embedding, retrieval, and reasoning using a pipeline based on LangChain + Gemini 1.5 Flash.

Key AI agent functionality includes:
- Gemini-powered contextual chat for question-answering
- Summarizer that generates topic-wise notes
- RAG-based quiz creation with vectorstore indexing (FAISS)
- PDF loader for ingesting learning content
- Persistent vector search using `index.faiss` and `index.pkl`

This project excites me because it brings together **LLM integration**, **RAG pipeline**, **vector search**, and **interactive UI** in a real-world ed-tech application. It reflects my end-to-end AI engineering skills and passion for building human-friendly tools with cutting-edge ML tech.

---

## ✨ Features

- 🧠 **Gemini + LangChain Agent** – For planning, summarizing, and QA.
- 📄 **PDF Summarization** – Upload a PDF and get summarized notes.
- ❓ **Quiz Generator** – Extracts 10+ MCQs per topic via context-aware Gemini agent.
- 🔎 **FAISS-based Search** – Efficient retrieval using `vectorstore.py`.
- 🧰 **RAG Pipeline** – Combines PDF content, embeddings, and LLMs.
- 🔧 **Full Python Backend** – Clean modular code for easy scaling.
- 📦 **Dependency Isolation** – Python `venv` with `requirements.txt`.

---

## 🧰 Tech Stack

| Layer         | Technology                      |
|---------------|----------------------------------|
| 🤖 AI Model   | Gemini 1.5 Flash (Google AI)     |
| 🔗 Framework  | LangChain                        |
| 📄 PDF Parser | PyMuPDF / pdf_loader.py          |
| 🔍 Retrieval  | FAISS Vector DB + Indexing       |
| 🧠 RAG Agent  | rag_pipeline.py                  |
| 🧩 Backend    | Python + FastAPI / Flask (as needed) |
| 🗃️ Storage    | Local vectorstore (FAISS)         |
| 🧪 Testing     | temp.pdf, uploaded.pdf samples    |

---

## 📂 Project Folder Structure
EduBot/
├── backend/
│ ├── config.py
│ ├── gemini_chat.py
│ ├── main.py
│ ├── pdf_loader.py
│ ├── rag_pipeline.py
│ ├── vectorstore.py
│ └── requirements.txt
├── db/
│ ├── index.faiss
│ └── index.pkl
├── frontend/
│ └── app.py
├── venv/
├── README.md
├── .gitignore
├── requirements.txt
├── temp.pdf
├── uploaded.pdf


---

## 🚀 How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/manivuppala124/EduBot.git
cd EduBot
```
### 2. Setup Virtual Environment
```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r backend/requirements.txt
```
### 3. Add Your Gemini API Key
```
GEMINI_API_KEY = "your_gemini_api_key"
```
### 4. Run Backend
```
cd backend
python main.py
```
### 5. Use Sample PDFs
Place temp.pdf or uploaded.pdf in the root and test PDF-based quiz generation.

🔮 Future Scope
✅ Web frontend (React/Flask hybrid)

✅ Authentication and user profiles

✅ Export results to PDF

✅ Gamified progress tracker

✅ Chat-based learning with memory


👨‍💻 Author
Vuppala Manikanta
B.Tech – CSE (AI & ML)

✨ Built with 💙 for the future of AI in education. If you find this project helpful, leave a ⭐️ and share!

---
