# main.py

from fastapi import FastAPI, File, UploadFile
from utils.pdf_utils import extract_text_from_pdf
from utils.resume_parser import parse_resume_text

app = FastAPI()

@app.post("/parse_resume/")
async def parse_resume(file: UploadFile = File(...)):
    # Save uploaded file temporarily
    file_location = f"uploaded_resumes/{file.filename}"
    with open(file_location, "wb") as f:
        f.write(await file.read())

    # Extract text from the uploaded PDF
    resume_text = extract_text_from_pdf(file_location)
    if resume_text:
        # Parse the extracted text
        parsed_data = parse_resume_text(resume_text)
        return {"parsed_data": parsed_data}
    else:
        return {"error": "Failed to extract text from the resume."}
