# 🎓 EduBot Pro - AI Document Assistant

**EduBot Pro** is an intelligent PDF document assistant that leverages **Google Gemini 1.5**, **LangChain**, and **RAG (Retrieval-Augmented Generation)** to provide instant answers from your documents. Built with a beautiful Streamlit frontend and FastAPI backend, it offers a seamless document analysis experience.

This is a production-ready AI application demonstrating end-to-end implementation of modern AI technologies for document intelligence.

---

## 🔥 Why EduBot Pro? (Project Overview)

EduBot Pro transforms how users interact with documents. Instead of manually searching through lengthy PDFs, users can simply upload a document and ask natural language questions to get instant, contextual answers. 

The application uses a sophisticated RAG pipeline that:
- **Chunks documents** intelligently for optimal processing
- **Creates vector embeddings** using Google's embedding models
- **Stores vectors** in FAISS for efficient similarity search
- **Generates contextual answers** using Gemini 1.5 Flash
- **Provides beautiful UI** with modern design principles

Key technical highlights include:
- Advanced document processing with configurable chunking
- FAISS-based vector storage for fast retrieval
- Gemini AI integration for natural language understanding
- Real-time document upload and processing
- Professional Streamlit interface with custom CSS

This project showcases my expertise in **LLM integration**, **vector databases**, **RAG architecture**, and **full-stack AI application development**.

---

## ✨ Features

- 🤖 **Gemini 1.5 Flash Integration** – Advanced AI for document understanding
- 📄 **PDF Document Processing** – Upload and analyze any PDF document
- 🔍 **Intelligent Q&A System** – Ask natural language questions about your documents
- 🧠 **RAG Pipeline** – Retrieval-Augmented Generation for accurate answers
- 💾 **FAISS Vector Storage** – Efficient similarity search and retrieval
- 🎨 **Beautiful UI** – Modern Streamlit interface with custom styling
- ⚡ **Real-time Processing** – Live upload progress and instant responses
- 📱 **Responsive Design** – Works seamlessly on desktop and mobile
- 🔄 **Session Management** – Maintains document state across interactions

---

## 🧰 Tech Stack

| Component | Technology |
|-----------|------------|
| 🤖 **AI Model** | Google Gemini 1.5 Flash |
| 🔗 **AI Framework** | LangChain |
| 🌐 **Backend** | FastAPI |
| 🖥️ **Frontend** | Streamlit |
| 📄 **PDF Processing** | PyPDF2, LangChain PDF Loader |
| 🔍 **Vector Database** | FAISS |
| 🧮 **Embeddings** | Google GenerativeAI Embeddings |
| 🎨 **Styling** | Custom CSS, Google Fonts |
| 📦 **Package Management** | pip, requirements.txt |

---

## 📂 Project Structure

```
EduBot/
├── backend/
│   ├── __pycache__/           # Python cache files
│   ├── config.py              # Configuration (API keys, settings)
│   ├── gemini_chat.py         # Gemini AI integration
│   ├── main.py                # FastAPI backend server
│   ├── pdf_loader.py          # PDF processing utilities
│   ├── rag_pipeline.py        # RAG implementation
│   ├── vectorstore.py         # FAISS vector operations
│   └── requirements.txt       # Backend dependencies
├── db/
│   ├── index.faiss           # FAISS vector index
│   └── index.pkl             # FAISS metadata
├── frontend/
│   └── app.py                # Streamlit application
├── .gitignore                # Git ignore patterns
├── how_to_run.txt           # Setup instructions
├── README.md                # Project documentation
├── requirements.txt         # Main dependencies
├── temp.pdf                 # Temporary PDF storage
└── uploaded.pdf             # User uploaded documents
```

---

## 🚀 Quick Start Guide

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/EduBot.git
cd EduBot
```

### 2. Set Up Python Environment
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Configure API Key
Edit `backend/config.py` and add your Google Gemini API key:
```python
GEMINI_API_KEY = "your_gemini_api_key_here"
```

### 4. Start the Backend Server
```bash
cd backend
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

### 5. Launch the Frontend
In a new terminal:
```bash
streamlit run frontend/app.py
```

### 6. Access the Application
Open your browser and go to: `http://localhost:8501`

---

## 🎯 How to Use

1. **Upload Document**: Click the upload area and select a PDF file
2. **Wait for Processing**: The system will process and index your document
3. **Ask Questions**: Type your question in the input field
4. **Get Answers**: Receive AI-generated answers based on your document content
5. **Explore Further**: Use sample questions or ask follow-up queries

### Sample Questions to Try:
- "What is the main topic of this document?"
- "Can you provide a summary of the key points?"
- "What are the important dates mentioned?"
- "Who are the main people or organizations discussed?"
- "What conclusions does the author draw?"

---

## ⚙️ Configuration Options

### Document Processing Settings (`config.py`):
```python
CHUNK_SIZE = 500        # Size of text chunks for processing
CHUNK_OVERLAP = 50      # Overlap between chunks for context
```

### Customization Options:
- **Chunk Size**: Adjust for different document types
- **Model Selection**: Switch between Gemini models
- **UI Themes**: Modify CSS for different appearances
- **Response Length**: Configure answer generation parameters

---

## 🔧 API Endpoints

### Backend Routes (FastAPI):

- **POST** `/upload-pdf/`
  - Upload and process PDF documents
  - Creates vector embeddings and stores in FAISS

- **POST** `/ask/`
  - Submit questions about uploaded documents
  - Returns AI-generated answers using RAG

---

## 🧪 Testing

### Test with Sample Documents:
1. Use the provided `temp.pdf` for initial testing
2. Try various document types (research papers, reports, manuals)
3. Test different question types (factual, analytical, summarization)

### Performance Considerations:
- **Document Size**: Optimal for documents under 50MB
- **Response Time**: Typically 3-5 seconds for complex queries
- **Accuracy**: Best with well-structured, text-heavy documents

---

## 🔮 Future Enhancements

### Planned Features:
- [ ] **Multi-document Support** - Query across multiple PDFs
- [ ] **Chat History** - Maintain conversation context
- [ ] **Document Comparison** - Compare multiple documents
- [ ] **Export Functionality** - Save Q&A sessions
- [ ] **User Authentication** - Personal document libraries
- [ ] **Advanced Analytics** - Document insights and metrics
- [ ] **Mobile App** - Native mobile experience
- [ ] **API Integration** - RESTful API for third-party integration

### Technical Improvements:
- [ ] **Caching System** - Redis for improved performance
- [ ] **Database Integration** - PostgreSQL for user data
- [ ] **Docker Containerization** - Easy deployment
- [ ] **Cloud Deployment** - AWS/GCP hosting
- [ ] **Advanced Chunking** - Semantic text splitting
- [ ] **Multi-language Support** - International document processing

---

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. **Fork the Repository**
2. **Create Feature Branch**: `git checkout -b feature/your-feature`
3. **Commit Changes**: `git commit -m 'Add your feature'`
4. **Push to Branch**: `git push origin feature/your-feature`
5. **Submit Pull Request**

### Development Guidelines:
- Follow PEP 8 style guidelines
- Add docstrings to new functions
- Include unit tests for new features
- Update documentation as needed

---

## 📋 Dependencies

### Main Libraries:
```
streamlit>=1.28.0          # Frontend framework
fastapi>=0.104.0           # Backend API framework
uvicorn>=0.24.0            # ASGI server
langchain>=0.0.330         # LLM framework
google-generativeai>=0.3.0 # Gemini AI integration
faiss-cpu>=1.7.4           # Vector similarity search
PyPDF2>=3.0.1              # PDF processing
python-multipart>=0.0.6    # File upload handling
requests>=2.31.0           # HTTP client
```

---

## 🐛 Troubleshooting

### Common Issues:

**1. API Key Errors**
- Ensure your Gemini API key is correctly set in `config.py`
- Verify the API key has necessary permissions

**2. Connection Errors**
- Check if FastAPI backend is running on port 8000
- Ensure no firewall blocking local connections

**3. PDF Processing Issues**
- Verify PDF is not password-protected
- Check file size (should be under 200MB)
- Ensure PDF contains extractable text

**4. Vector Store Errors**
- Delete `db/` folder and re-upload documents
- Check file permissions in project directory

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Vuppala Manikanta**  
B.Tech – Computer Science & Engineering (AI & ML)

- 📧 Email: [manikantavuppala124@gmail.com]
- 💼 LinkedIn: [https://www.linkedin.com/in/vuppala-manikanta-504596314]
- 🐱 GitHub: [https://github.com/manivuppala124/]

---

## 🙏 Acknowledgments

- **Google AI** for providing the Gemini API
- **LangChain** for the excellent framework
- **Streamlit** for the beautiful frontend capabilities
- **FastAPI** for the robust backend framework
- **FAISS** for efficient vector search capabilities

---

## ⭐ Support

If you find this project helpful:
- ⭐ **Star the repository**
- 🍴 **Fork and contribute**
- 📢 **Share with others**
- 🐛 **Report issues**

---

**Built with 💙 for the future of AI-powered document intelligence.**

*Last updated: June 2025*
