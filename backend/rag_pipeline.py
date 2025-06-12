# backend/rag_pipeline.py

from backend.vectorstore import load_vectorstore
from backend.gemini_chat import ask_gemini

def get_qa_chain():
    return load_vectorstore().as_retriever()

def generate_answer(retriever, question):
    try:
        docs = retriever.get_relevant_documents(question)
        context = "\n".join([doc.page_content for doc in docs])
        return ask_gemini(context, question)
    except Exception as e:
        return f"❌ RAG Pipeline error: {str(e)}"
