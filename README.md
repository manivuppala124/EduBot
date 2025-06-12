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



## 🔑 Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/manivuppala124/EduBot.git
cd EduBot
2. Set up the Backend
cd backend
npm install
touch .env
📄 .env Example
env
Copy
Edit
PORT=5000
DATABASE_URL=postgres://<username>:<password>@localhost:5432/edubot
GEMINI_API_KEY=your_gemini_api_key_here
📦 Run Prisma & Start Server
npx prisma generate
npx prisma migrate dev --name init
npm run dev
3. Set up the Frontend
cd ../frontend
npm install
npm run dev
🤖 Gemini 1.5 API Setup
🔗 Get Gemini API Key
Go to 👉 https://makersuite.google.com/app

Create a project and get your API Key

Add it to your .env file as GEMINI_API_KEY

📂 Project Folder Structure
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
 Future Scope
✅ User Authentication

✅ Export quizzes to PDF

✅ Voice-based quiz generator

✅ Daily MCQ challenge feature

✅ Gamified learning dashboard

✅ Chat-based quiz assistant

📜 License
This project is licensed under the MIT License.
Feel free to use, fork, and contribute ❤️

🙏 Acknowledgements
Google Gemini 1.5

LangChain

Cohere AI

Striver DSA Sheet

Vite + React

👨‍💻 Author
Vuppala Manikanta
B.Tech – CSE (AI & ML)
📬 LinkedIn
💻 GitHub

✨ Built with 💙 for the future of AI in education. If you find this project helpful, leave a ⭐️ and share!

---

Manikanta, this is all ready to impress recruiters and your peers! Let me know if you'd like help with a GitHub action for deployment or a `TaskAgent` README next!  
Good luck next challenges and tips to remember well and perform well in academics and your skills 🙏🏻🔥
