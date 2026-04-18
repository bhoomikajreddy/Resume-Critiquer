# ai-resume-critiquer

Built an AI-powered Resume Critiquer using Streamlit and OpenAI that analyzes resumes, understands context, and provides actionable feedback to improve structure, content, and job relevance.

The app allows users to upload their resume (PDF/TXT), optionally specify a job role, and receive personalized suggestions to make their resume more impactful and ATS-friendly.

---

## Highlights

- Upload resumes in PDF or TXT format
- Extracts and processes resume content using PyPDF2
- Uses OpenAI to generate intelligent, context-aware feedback
- Provides suggestions on:
  - Formatting
  - Content clarity
  - Keyword optimization
- Optional job role input for targeted recommendations
- Simple and interactive UI built with Streamlit

---

## Tech Stack

- streamlit: used to build the interactive web UI  
- openai: used for generating resume feedback  
- PyPDF2: used for extracting text from PDF resumes  
- dotenv: used to securely manage API keys  
- python: core programming language  

---

## How it works

1. User uploads resume  
2. Text is extracted from file  
3. Prompt is generated with optional job role  
4. OpenAI model analyzes resume  
5. Feedback is displayed in the UI  

---

<img width="955" height="733" alt="Resume Critiquer" src="https://github.com/user-attachments/assets/a89873b0-b987-4faf-ab9b-c34cfb2b13a7" />

<img width="962" height="503" alt="Analyze Response" src="https://github.com/user-attachments/assets/b832a984-f4b6-4f60-be4f-e905e287f7bb" />
