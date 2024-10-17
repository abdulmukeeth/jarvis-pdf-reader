# jarvis-pdf-reader 
Jarvis: The PDF Guru
Jarvis is a PDF-based chatbot built using Streamlit, LangChain, and Gemini LLM. It allows users to upload a PDF document, ask questions about its content, and get relevant answers. The chatbot processes the PDF content locally and ensures that only PDF-relevant questions are answered.

Features
PDF Upload: Upload any PDF document to interact with.
Question Answering: Ask questions related to the uploaded PDF, and the chatbot will provide contextually relevant answers based on the document.
Continuous Chat: Displays chat history above the input area, allowing users to have a continuous conversation with the PDF content.
Enter Key Submission: Users can submit their questions by pressing Enter, making the interaction smooth and user-friendly.
Tech Stack
Python: Core language for building the application.
Streamlit: Frontend framework for creating the user interface.
LangChain: For handling prompts and managing interactions between the PDF content and the language model.
Gemini LLM: The underlying large language model used for generating responses.
PyPDF2: For processing and extracting text from the PDF files.
Installation
Prerequisites
Python 3.8 or above
Pip (Python package manager)
Gemini API key for accessing the Gemini LLM
