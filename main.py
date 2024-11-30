import spacy
from fastapi import FastAPI, File, UploadFile, HTTPException
from pydantic import BaseModel
from typing import List, Dict
import PyPDF2
import os

# Initialize FastAPI app
app = FastAPI()

# Load the spaCy model (English)
nlp = spacy.load("en_core_web_sm")

# Directory to store uploaded resumes
UPLOAD_DIR = "uploaded_resumes"

# Create upload directory if it doesn't exist
os.makedirs(UPLOAD_DIR, exist_ok=True)

# Model to define the structure of request payload for parsing
class ResumeParseRequest(BaseModel):
    file: UploadFile

# Function to extract text from PDF
def extract_text_from_pdf(pdf_file_path: str) -> str:
    try:
        with open(pdf_file_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            text = ""
            for page in range(len(reader.pages)):
                text += reader.pages[page].extract_text()
            return text
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error extracting PDF: {e}")

# Function to extract relevant information from resume text
def parse_resume(text: str) -> Dict[str, str]:
    doc = nlp(text)

    # Example: Extract name, contact details, skills, etc.
    resume_data = {
        "name": "N/A",
        "email": "N/A",
        "phone": "N/A",
        "skills": [],
        "experience": [],
        "education": []
    }

    for ent in doc.ents:
        if ent.label_ == "PERSON":
            resume_data["name"] = ent.text
        elif ent.label_ == "EMAIL":
            resume_data["email"] = ent.text
        elif ent.label_ == "PHONE":
            resume_data["phone"] = ent.text

    # Example: Extract skills (can be expanded based on custom knowledge base)
    skills_keywords = ["Python", "Java", "JavaScript", "C++", "SQL", "Machine Learning"]
    resume_data["skills"] = [skill for skill in skills_keywords if skill.lower() in text.lower()]

    # Example: Extract experience or education (you can enhance this part with more NLP techniques)
    for sentence in doc.sents:
        if "years of experience" in sentence.text.lower():
            resume_data["experience"].append(sentence.text)
        elif "university" in sentence.text.lower() or "degree" in sentence.text.lower():
            resume_data["education"].append(sentence.text)

    return resume_data

# API endpoint for uploading and parsing resume
@app.post("/parse_resume/")
async def parse_resume_endpoint(file: UploadFile = File(...)):
    file_location = os.path.join(UPLOAD_DIR, file.filename)

    # Save the uploaded file
    with open(file_location, "wb") as f:
        f.write(await file.read())

    # Extract text from the uploaded PDF resume
    if file.filename.lower().endswith(".pdf"):
        resume_text = extract_text_from_pdf(file_location)
    else:
        raise HTTPException(status_code=400, detail="Only PDF files are supported.")
    
    # Parse the resume to extract details
    parsed_data = parse_resume(resume_text)

    # Optionally delete the uploaded file after parsing
    os.remove(file_location)

    return {"parsed_data": parsed_data}

# Example of running the FastAPI app:
# To run the app, use the command:
# uvicorn main:app --reload
