# job-portal-resume-parser

A powerful Resume Parser AI built using FastAPI and spaCy for extracting key information such as name, email, phone, skills, experience, and education from uploaded resume files (in PDF format).

Features
Resume Upload: Users can upload resumes (PDF format).
Resume Parsing: Extract key details such as name, contact information, skills, experience, and education.
FastAPI Endpoint: The application exposes an API endpoint to parse the uploaded resumes.
spaCy NLP: Utilizes spaCy for Natural Language Processing (NER) to identify key information from resumes.
Requirements
Python 3.7+
spaCy
FastAPI
Uvicorn (for running the FastAPI server)
PyPDF2 (for PDF text extraction)
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/resume-parser-ai.git
cd resume-parser-ai
Create and activate a virtual environment (optional but recommended):

bash
Copy code
python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
Install required dependencies:

bash
Copy code
pip install -r requirements.txt
Install spaCy language model:

bash
Copy code
python -m spacy download en_core_web_sm
Project Structure
bash
Copy code
resume-parser-ai/
│
├── main.py                  # FastAPI app with resume parsing logic
├── requirements.txt         # Python dependencies
├── README.md                # Project documentation
└── uploaded_resumes/        # Directory to store uploaded resume files
Running the Application
Start the FastAPI server:

bash
Copy code
uvicorn main:app --reload
The application will be available at http://127.0.0.1:8000.

Test the Resume Parser API:

You can test the resume parser using tools like Postman or curl by sending a POST request to http://127.0.0.1:8000/parse_resume/.

Request Body:

Use form-data with the key file and upload a PDF resume.
Response:

The API will return a JSON object with the parsed details, like this:

json
Copy code
{
  "parsed_data": {
    "name": "John Doe",
    "email": "john.doe@example.com",
    "phone": "1234567890",
    "skills": ["Python", "Machine Learning"],
    "experience": ["5 years of experience in software development"],
    "education": ["Bachelor's degree in Computer Science from ABC University"]
  }
}
API Documentation
POST /parse_resume/: Uploads a resume (PDF format) and returns parsed information such as name, email, phone, skills, experience, and education.

Request:

file: The resume PDF file.
Response:

A JSON object containing the parsed resume data, such as name, email, phone, skills, experience, and education.
Example cURL Request
You can also test the API with curl:

bash
Copy code
curl -X 'POST' \
  'http://127.0.0.1:8000/parse_resume/' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@path/to/your/resume.pdf'
Enhancements
Support for more file formats: The current version supports PDF files. Future versions can extend support to DOCX, TXT, and other formats.
Improved NLP: Customize or train a specific NLP model for more accurate extraction (e.g., skills, work experience, education).
Error Handling: Add more detailed error messages and validations.
Integration with Job Portals: This API can be integrated with job portals to automatically extract and store resume data.
License
This project is licensed under the MIT License - see the LICENSE file for details.

Contributing
Feel free to submit issues, feature requests, or pull requests if you wish to contribute to the project. Please make sure to follow the coding conventions and write tests where necessary.
