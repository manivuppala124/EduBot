# 🤖 EduBot – Personalized AI Learning Assistant using Gemini 1.5 + LangChain

EduBot is an intelligent AI-powered quiz and learning assistant that generates MCQs and personalized learning content based on user-selected topics or input content. It leverages Google’s **Gemini 1.5 Flash model**, **LangChain**, and advanced summarization techniques to deliver a smart, responsive, and engaging ed-tech experience.

---

## ✨ Features

- 🔍 **Topic-Based Quiz Generation**  
  Generate 10+ MCQs per topic using context-aware AI.

- 📄 **Smart Summarizer**  
  Summarize lengthy study material into clear, concise points.

- 📊 **Performance Tracker**  
  Records user scores and progress using PostgreSQL.

- 🧠 **AI-Powered Agent**  
  Uses Gemini 1.5 + LangChain tools for planning and reasoning.

- 💾 **Database-Backed**  
  Persistent storage using PostgreSQL for scalability.

- 💻 **Modern Fullstack App**  
  React + Vite frontend, Node.js + TypeScript backend.

---

## 🧰 Tech Stack

| Layer       | Technology                          |
|-------------|-------------------------------------|
| 🧠 AI Model | Gemini 1.5 Flash (Google AI Studio) |
| 🧩 Backend  | Node.js + Express + TypeScript      |
| 🎨 Frontend | React.js + Vite + TypeScript        |
| 🗄 Database | PostgreSQL                          |
| 🔐 Auth     | JWT (optional)                      |
| ⚙️ API Use  | LangChain, Gemini, Cohere (optional)|

---

## 🔑 Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/manivuppala124/EduBot.git
cd EduBot
2. Set up the Backend
bash
Copy
Edit
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
bash
Copy
Edit
npx prisma generate
npx prisma migrate dev --name init
npm run dev
3. Set up the Frontend
bash
Copy
Edit
cd ../frontend
npm install
npm run dev
🤖 Gemini 1.5 API Setup
🔗 Get Gemini API Key
Go to 👉 https://makersuite.google.com/app

Create a project and get your API Key

Add it to your .env file as GEMINI_API_KEY

📂 Project Folder Structure
css
Copy
Edit
EduBot/
├── backend/
│   ├── routes/
│   ├── controllers/
│   ├── services/
│   ├── prisma/
│   └── index.ts
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/
│   │   └── App.tsx
└── README.md🔮```
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
