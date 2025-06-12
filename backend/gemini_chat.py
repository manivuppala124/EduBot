# backend/gemini_chat.py

import google.generativeai as genai
from backend.config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

# Use a free-tier supported model
model = genai.GenerativeModel("models/gemini-1.5-flash")

def ask_gemini(context, question):
    prompt = f"""
    You are a helpful assistant. Answer the question based on the context below.

    Context:
    {context}

    Question:
    {question}

    Answer:"""

    try:
        response = model.generate_content(prompt)
        return response.text if response and hasattr(response, "text") else "❌ Gemini returned no response."
    except Exception as e:
        return f"❌ Gemini error: {str(e)}"
