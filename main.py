import streamlit as st
from langchain_core.prompts import PromptTemplate
from gemini_llm import GeminiLLM
import warnings
import PyPDF2

warnings.filterwarnings("ignore", category=UserWarning)

# Function to process PDF
def extract_pdf_content(pdf_file):
    reader = PyPDF2.PdfReader(pdf_file)
    pdf_text = ''
    for page_num in range(len(reader.pages)):
        page = reader.pages[page_num]
        pdf_text += page.extract_text()
    return pdf_text

# Function to check if the question is relevant to the PDF content
def is_question_relevant(question, pdf_content):
    keywords = pdf_content.split()  # Split PDF content into words
    question_words = question.split()  # Split question into words
    return any(word in keywords for word in question_words)

# Function to handle question submission
def handle_question_submission(pdf_content):
    question = st.session_state["question_input"]
    
    if question:
        # Initialize the custom Gemini LLM
        gemini_llm = GeminiLLM()

        # Define a prompt template
        prompt_template = PromptTemplate(
            input_variables=["question", "pdf_content"],
            template="Answer the question based on the following document:\n\n{pdf_content}\n\nQuestion:\n{question}"
        )

        # Define the new way of chaining using `|`
        prompt_llm_chain = prompt_template | gemini_llm

        # Check if the question is relevant to the PDF content
        if is_question_relevant(question, pdf_content):
            # Get the answer from the LLM
            answer = prompt_llm_chain.invoke({"question": question, "pdf_content": pdf_content})
            # Add the question and answer to chat history
            st.session_state.chat_history.append((question, answer))
        else:
            st.session_state.chat_history.append((question, "I can only answer questions related to the PDF."))

        # Clear the input box after submission
        st.session_state["question_input"] = ""  # Reset the input box

def main():
    st.title("Jarvis: The PDF Guru")

    # Initialize session state to store chat history
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # Upload the PDF file
    pdf_file = st.file_uploader("Upload a PDF", type=["pdf"])
    
    if pdf_file:
        # Extract PDF content
        pdf_content = extract_pdf_content(pdf_file)
        st.success("PDF uploaded and processed successfully!")

        # Display chat history above the input box
        if st.session_state.chat_history:
            for q, a in st.session_state.chat_history:
                st.write(f"**You:** {q}")
                st.write(f"**Assistant:** {a}")
                st.write("---")  # Divider between questions

        # Display the input text area for the question and handle enter key submission
        st.text_input(
            "Ask a question related to the PDF",
            key="question_input",
            on_change=handle_question_submission,
            args=(pdf_content,),
            placeholder="Type your question and press Enter"
        )
    else:
        st.info("Please upload a PDF file.")

if __name__ == "__main__":
    main()
