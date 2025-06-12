import streamlit as st
import requests
import html
import time
from datetime import datetime

# ===================== PAGE CONFIG =====================
st.set_page_config(
    page_title="EduBot Pro - AI Document Assistant",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ===================== CUSTOM CSS =====================
st.markdown("""
<style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* Global Styles */
    .stApp {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }
    
    /* Hide Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Main container */
    .main-container {
        max-width: 1000px;
        margin: 0 auto;
        padding: 2rem 1rem;
    }
    
    /* Header styling */
    .header-container {
        text-align: center;
        margin-bottom: 3rem;
        padding: 2rem;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 20px;
        color: white;
        box-shadow: 0 20px 40px rgba(102, 126, 234, 0.2);
    }
    
    .header-title {
        font-size: 3.5rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
        text-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    .header-subtitle {
        font-size: 1.3rem;
        font-weight: 300;
        opacity: 0.9;
        margin-bottom: 0;
    }
    
    /* Card styles */
    .card {
        background: white;
        border-radius: 16px;
        padding: 2rem;
        margin: 1rem 0;
        box-shadow: 0 8px 32px rgba(0,0,0,0.08);
        border: 1px solid rgba(255,255,255,0.1);
        transition: all 0.3s ease;
    }
    
    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 16px 48px rgba(0,0,0,0.12);
    }
    
    .card-header {
        display: flex;
        align-items: center;
        margin-bottom: 1.5rem;
        padding-bottom: 1rem;
        border-bottom: 2px solid #f0f2f6;
    }
    
    .card-icon {
        font-size: 2rem;
        margin-right: 1rem;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    .card-title {
        font-size: 1.5rem;
        font-weight: 600;
        color: #2d3748;
        margin: 0;
    }
    
    /* Upload area styling */
    .upload-area {
        border: 2px dashed #cbd5e0;
        border-radius: 12px;
        padding: 3rem 2rem;
        text-align: center;
        background: #f7fafc;
        transition: all 0.3s ease;
        margin: 1rem 0;
    }
    
    .upload-area:hover {
        border-color: #667eea;
        background: #edf2f7;
    }
    
    /* Success/Error messages */
    .success-message {
        background: linear-gradient(135deg, #48bb78 0%, #38a169 100%);
        color: white;
        padding: 1rem 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
        display: flex;
        align-items: center;
        font-weight: 500;
        box-shadow: 0 4px 16px rgba(72, 187, 120, 0.3);
    }
    
    .error-message {
        background: linear-gradient(135deg, #f56565 0%, #e53e3e 100%);
        color: white;
        padding: 1rem 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
        display: flex;
        align-items: center;
        font-weight: 500;
        box-shadow: 0 4px 16px rgba(245, 101, 101, 0.3);
    }
    
    .warning-message {
        background: linear-gradient(135deg, #ed8936 0%, #dd6b20 100%);
        color: white;
        padding: 1rem 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
        display: flex;
        align-items: center;
        font-weight: 500;
        box-shadow: 0 4px 16px rgba(237, 137, 54, 0.3);
    }
    
    /* Answer styling */
    .answer-container {
        background: linear-gradient(135deg, #f7fafc 0%, #edf2f7 100%);
        border: 1px solid #e2e8f0;
        border-radius: 16px;
        padding: 2rem;
        margin: 2rem 0;
        position: relative;
        overflow: hidden;
    }
    
    .answer-container::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 4px;
        height: 100%;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    .answer-header {
        display: flex;
        align-items: center;
        margin-bottom: 1rem;
        color: #4a5568;
        font-weight: 600;
    }
    
    .answer-text {
        font-size: 1.1rem;
        line-height: 1.7;
        color: #2d3748;
        margin: 0;
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 0.75rem 2rem;
        font-weight: 600;
        font-size: 1rem;
        transition: all 0.3s ease;
        box-shadow: 0 4px 16px rgba(102, 126, 234, 0.3);
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 24px rgba(102, 126, 234, 0.4);
    }
    
    /* Input styling */
    .stTextInput > div > div > input {
        border-radius: 12px;
        border: 2px solid #e2e8f0;
        padding: 1rem;
        font-size: 1rem;
        transition: all 0.3s ease;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #667eea;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
    }
    
    /* Progress bar */
    .stProgress > div > div {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 8px;
    }
    
    /* Footer */
    .footer {
        text-align: center;
        margin-top: 4rem;
        padding: 2rem;
        background: #f7fafc;
        border-radius: 16px;
        color: #718096;
        font-size: 0.9rem;
    }
    
    .footer-link {
        color: #667eea;
        text-decoration: none;
        font-weight: 500;
    }
    
    .footer-link:hover {
        color: #764ba2;
    }
    
    /* Responsive design */
    @media (max-width: 768px) {
        .header-title {
            font-size: 2.5rem;
        }
        
        .header-subtitle {
            font-size: 1.1rem;
        }
        
        .card {
            padding: 1.5rem;
        }
        
        .upload-area {
            padding: 2rem 1rem;
        }
    }
    
    /* Animation classes */
    .fade-in {
        animation: fadeIn 0.6s ease-in;
    }
    
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
</style>
""", unsafe_allow_html=True)

# ===================== HEADER =====================
st.markdown("""
<div class="header-container fade-in">
    <div class="header-title">🎓 EduBot Pro</div>
    <div class="header-subtitle">Your Intelligent PDF Assistant</div>
</div>
""", unsafe_allow_html=True)

# Initialize session state
if 'pdf_uploaded' not in st.session_state:
    st.session_state.pdf_uploaded = False
if 'pdf_name' not in st.session_state:
    st.session_state.pdf_name = ""

# ===================== PDF UPLOAD SECTION =====================
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("""
    <div class="card fade-in">
        <div class="card-header">
            <div class="card-icon">📤</div>
            <div class="card-title">Upload Your Document</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    pdf = st.file_uploader(
        "",
        type=["pdf"],
        help="Select a PDF document to analyze. Maximum file size: 200MB",
        label_visibility="collapsed"
    )

with col2:
    if st.session_state.pdf_uploaded:
        st.markdown("""
        <div class="success-message">
            <span style="margin-right: 0.5rem;">✅</span>
            <span>Document Ready!</span>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
        <div style="padding: 1rem; background: #e6fffa; border-radius: 8px; margin-top: 1rem;">
            <strong>📄 {st.session_state.pdf_name}</strong><br>
            <small style="color: #38a169;">Uploaded at {datetime.now().strftime('%H:%M:%S')}</small>
        </div>
        """, unsafe_allow_html=True)

# Handle PDF upload
if pdf and not st.session_state.pdf_uploaded:
    st.session_state.pdf_name = pdf.name
    
    with open("uploaded.pdf", "wb") as f:
        f.write(pdf.read())
    
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    with st.spinner(""):
        try:
            # Simulate processing steps
            for i in range(20, 60, 10):
                progress_bar.progress(i)
                status_text.text(f"🔄 Processing document... {i}%")
                time.sleep(0.2)
            
            response = requests.post(
                "http://127.0.0.1:8000/upload-pdf/",
                files={"file": open("uploaded.pdf", "rb")}
            )
            
            for i in range(60, 100, 10):
                progress_bar.progress(i)
                status_text.text(f"🔄 Finalizing... {i}%")
                time.sleep(0.1)
            
            progress_bar.progress(100)
            
            if response.status_code == 200:
                res_json = response.json()
                if "✅" in res_json.get("status", ""):
                    status_text.empty()
                    progress_bar.empty()
                    st.session_state.pdf_uploaded = True
                    st.success("🎉 Document uploaded successfully!")
                    time.sleep(1)
                    st.rerun()
                else:
                    st.markdown(f"""
                    <div class="error-message">
                        <span style="margin-right: 0.5rem;">❌</span>
                        <span>Upload failed: {res_json.get("status", "Unknown error")}</span>
                    </div>
                    """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div class="error-message">
                    <span style="margin-right: 0.5rem;">❌</span>
                    <span>Server Error {response.status_code}</span>
                </div>
                """, unsafe_allow_html=True)
                st.code(response.text)
                
        except Exception as e:
            st.markdown(f"""
            <div class="error-message">
                <span style="margin-right: 0.5rem;">🔌</span>
                <span>Connection Error: {str(e)}</span>
            </div>
            """, unsafe_allow_html=True)
        finally:
            progress_bar.empty()
            status_text.empty()

# ===================== QUESTION SECTION =====================
if st.session_state.pdf_uploaded:
    st.markdown("---")
    
    st.markdown("""
    <div class="card fade-in">
        <div class="card-header">
            <div class="card-icon">💬</div>
            <div class="card-title">Ask Your Question</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Question input with suggestions
    col1, col2 = st.columns([3, 1])
    
    with col1:
        user_question = st.text_input(
            "",
            placeholder="What would you like to know about this document?",
            help="Ask specific questions about the content, request summaries, or seek clarifications",
            label_visibility="collapsed"
        )
    
    with col2:
        ask_button = st.button("🚀 Ask EduBot", use_container_width=True)
    
    # Sample questions
    with st.expander("💡 Need inspiration? Try these sample questions"):
        sample_questions = [
            "What is the main topic of this document?",
            "Can you provide a summary of the key points?",
            "What are the important dates mentioned?",
            "Who are the main people or organizations discussed?",
            "What conclusions does the author draw?"
        ]
        
        for i, question in enumerate(sample_questions):
            if st.button(f"📝 {question}", key=f"sample_{i}"):
                user_question = question
                ask_button = True
    
    # Handle question submission
    if ask_button or user_question:
        if not user_question or not user_question.strip():
            st.markdown("""
            <div class="warning-message">
                <span style="margin-right: 0.5rem;">⚠️</span>
                <span>Please enter a valid question to continue.</span>
            </div>
            """, unsafe_allow_html=True)
        else:
            # Create thinking animation
            thinking_placeholder = st.empty()
            
            with thinking_placeholder:
                st.markdown("""
                <div style="text-align: center; padding: 2rem;">
                    <div style="font-size: 3rem; animation: pulse 1.5s infinite;">🤖</div>
                    <div style="font-size: 1.2rem; color: #667eea; margin-top: 1rem;">
                        EduBot is analyzing your question...
                    </div>
                </div>
                """, unsafe_allow_html=True)
            
            try:
                answer_response = requests.post(
                    "http://127.0.0.1:8000/ask/",
                    data={"question": user_question}
                )
                
                thinking_placeholder.empty()
                
                if answer_response.status_code == 200:
                    result = answer_response.json()
                    answer_text = result.get("answer", "").strip()
                    
                    if not answer_text:
                        st.markdown("""
                        <div class="error-message">
                            <span style="margin-right: 0.5rem;">❌</span>
                            <span>No answer was generated. Please try rephrasing your question.</span>
                        </div>
                        """, unsafe_allow_html=True)
                    elif "❌" in answer_text or "cannot answer" in answer_text.lower():
                        st.markdown(f"""
                        <div class="warning-message">
                            <span style="margin-right: 0.5rem;">⚠️</span>
                            <span>{html.escape(answer_text)}</span>
                        </div>
                        """, unsafe_allow_html=True)
                    else:
                        # Display the answer beautifully
                        clean_answer = html.escape(answer_text).replace("\n", "<br>")
                        st.markdown(f"""
                        <div class="answer-container fade-in">
                            <div class="answer-header">
                                <span style="font-size: 1.5rem; margin-right: 0.5rem;">🧠</span>
                                EduBot's Answer
                            </div>
                            <div class="answer-text">{clean_answer}</div>
                        </div>
                        """, unsafe_allow_html=True)
                        
                        # Add helpful actions
                        col1, col2, col3 = st.columns(3)
                        with col1:
                            st.button("👍 Helpful", help="Mark this answer as helpful")
                        with col2:
                            st.button("🔄 Ask Follow-up", help="Ask a related question")
                        with col3:
                            st.button("📋 Copy Answer", help="Copy answer to clipboard")
                            
                else:
                    st.markdown(f"""
                    <div class="error-message">
                        <span style="margin-right: 0.5rem;">⚠️</span>
                        <span>Backend error: {answer_response.status_code}</span>
                    </div>
                    """, unsafe_allow_html=True)
                    with st.expander("View error details"):
                        st.code(answer_response.text)
                        
            except Exception as e:
                thinking_placeholder.empty()
                st.markdown(f"""
                <div class="error-message">
                    <span style="margin-right: 0.5rem;">🔌</span>
                    <span>Connection error: {str(e)}</span>
                </div>
                """, unsafe_allow_html=True)

# ===================== FOOTER =====================
st.markdown("""
<div class="footer">
    <div style="font-size: 1.1rem; margin-bottom: 0.5rem;">
        🚀 Built with FastAPI • LangChain • Gemini AI
    </div>
    <div>
        Crafted with ❤️ by <a href="#" class="footer-link">Manikanta</a> • 
        <a href="#" class="footer-link">Documentation</a> • 
        <a href="#" class="footer-link">Support</a>
    </div>
</div>
""", unsafe_allow_html=True)

# Add some breathing room
st.markdown("<br><br>", unsafe_allow_html=True)