# backend/pdf_loader.py

from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from backend.config import CHUNK_SIZE, CHUNK_OVERLAP

def load_and_split_pdf(file_path):
    loader = PyPDFLoader(file_path)
    documents = loader.load()

    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
    )
    return text_splitter.split_documents(documents)
