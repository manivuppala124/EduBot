from fastapi import FastAPI, File, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from backend.pdf_loader import load_and_split_pdf
from backend.vectorstore import save_to_faiss
from backend.rag_pipeline import get_qa_chain, generate_answer
import shutil

app = FastAPI()

# ✅ Add CORS middleware here
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 🔒 For production, use your frontend domain like ["https://yourfrontend.com"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/upload-pdf/")
async def upload_pdf(file: UploadFile = File(...)):
    try:
        with open("temp.pdf", "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        chunks = load_and_split_pdf("temp.pdf")
        save_to_faiss(chunks)

        return {"status": "✅ Vector DB created successfully!"}
    except Exception as e:
        return {"status": f"❌ Upload failed: {str(e)}"}

@app.post("/ask/")
async def ask_question(question: str = Form(...)):
    try:
        retriever = get_qa_chain()
        answer = generate_answer(retriever, question)
        return {"answer": answer}
    except Exception as e:
        return {"answer": f"❌ Error generating answer: {str(e)}"}
