# job-portal-resume-parser

A powerful Resume Parser AI built using FastAPI and spaCy for extracting key information such as name, email, phone, skills, experience, and education from uploaded resume files (in PDF format).

## Features

- **Resume Upload**: Users can upload resumes (PDF format).
- **Resume Parsing**: Extract key details such as name, contact information, skills, experience, and education.
- **FastAPI Endpoint**: The application exposes an API endpoint to parse the uploaded resumes.
- **spaCy NLP**: Utilizes spaCy for Natural Language Processing (NER) to identify key information from resumes.

## Requirements

- Python 3.7+
- spaCy
- FastAPI
- Uvicorn (for running the FastAPI server)
- PyPDF2 (for PDF text extraction)
  
job-portal-resume-parser/
│
├── main.py                  # FastAPI app with resume parsing logic
├── requirements.txt         # Python dependencies
├── README.md                # Project documentation
├── uploaded_resumes/        # Directory to store uploaded resume files
└── utils/                   # Utility folder
    ├── __init__.py          # Make this a package
    ├── resume_parser.py     # Logic for parsing the resume
    └── pdf_utils.py         # Utility for extracting text from PDFs

