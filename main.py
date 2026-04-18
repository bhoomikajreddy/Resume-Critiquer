import streamlit as st
import PyPDF2
import io
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="AI Resume Critiquer", page_icon="📃", layout="centered")

st.title("AI Resume Critiquer")
st.markdown("Upload your resume in PDF format, and get instant feedback on how to improve it!")
st.text("This tool uses OpenAI's language model to analyze your resume and provide actionable suggestions for improvement.")

OpenAI_API_KEY = os.getenv("OPENAI_API_KEY")

uploaded_file = st.file_uploader("Upload your resume (PDF or TXT)", type=["pdf", "txt"])
job_role = st.text_input("Enter the job role you're applying for (optional)")

analyze = st.button("Analyze Resume")

def extract_text_from_pdf(pdf_file):
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text() + "\n"
    return text

def extract_text_from_file(uploaded_file):
    if uploaded_file.type == "application/pdf":
        return extract_text_from_pdf(io.BytesIO(uploaded_file.read()))
    return uploaded_file.read().decode("utf-8")
    
if analyze and uploaded_file:
    try:
        file__content = extract_text_from_file(uploaded_file)

        if not file__content.strip():
            st.error("The uploaded file is empty. Please upload a valid resume.")
            st.stop()

        prompt = f"""You are a career coach and resume expert. Analyze the following resume and provide feedback on how to improve it, especially for the job role: {job_role if job_role else 'general job applications'}.
        
        Resume Content:
        {file__content}

        Provide specific suggestions on formatting, content, and keywords to make the resume more effective."""

        client = OpenAI(api_key=OpenAI_API_KEY)
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful and knowledgeable career coach who provides constructive feedback on resumes."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=1000
        )
        st.markdown("### Resume Analysis and Feedback:")
        st.markdown(response.choices[0].message.content)
    except Exception as e:
        st.error(f"An error occurred while processing the resume: {str(e)}")