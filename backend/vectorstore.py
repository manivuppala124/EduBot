# backend/vectorstore.py

from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from backend.config import GEMINI_API_KEY

def save_to_faiss(chunks, db_path="db"):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=GEMINI_API_KEY)
    vectorstore = FAISS.from_documents(chunks, embeddings)
    vectorstore.save_local(db_path)

def load_vectorstore(db_path="db"):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=GEMINI_API_KEY)
    return FAISS.load_local(db_path, embeddings, allow_dangerous_deserialization=True)
