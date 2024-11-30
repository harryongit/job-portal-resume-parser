# utils/resume_parser.py

import spacy
import re

# Load the spaCy English model for named entity recognition
nlp = spacy.load("en_core_web_sm")

# Function to parse resume text
def parse_resume_text(resume_text):
    doc = nlp(resume_text)
    
    # Initialize empty result dictionary
    parsed_data = {
        "name": None,
        "email": None,
        "phone": None,
        "skills": [],
        "experience": [],
        "education": [],
    }
    
    # Extract named entities (like names, phone numbers, and emails)
    for ent in doc.ents:
        if ent.label_ == "PERSON" and not parsed_data["name"]:
            parsed_data["name"] = ent.text.strip()
        elif ent.label_ == "EMAIL" and not parsed_data["email"]:
            parsed_data["email"] = ent.text.strip()
        elif ent.label_ == "PHONE" and not parsed_data["phone"]:
            parsed_data["phone"] = ent.text.strip()

    # Extract skills, experience, and education based on custom rules
    # Example: matching keywords or regular expressions for skills and experiences
    parsed_data["skills"] = extract_skills(resume_text)
    parsed_data["experience"] = extract_experience(resume_text)
    parsed_data["education"] = extract_education(resume_text)
    
    return parsed_data


def extract_skills(resume_text):
    skills_keywords = ["Python", "Java", "C++", "SQL", "Machine Learning", "Data Science", "Project Management"]
    skills = []

    # Search for skills in the resume text
    for skill in skills_keywords:
        if skill.lower() in resume_text.lower():
            skills.append(skill)

    return skills


def extract_experience(resume_text):
    experience = []
    
    # Example pattern to capture experience-related text (e.g., work experience)
    experience_keywords = ["experience", "years of experience", "worked at", "interned at"]
    
    for keyword in experience_keywords:
        if keyword.lower() in resume_text.lower():
            experience.append(resume_text.lower().split(keyword)[-1].strip())

    return experience


def extract_education(resume_text):
    education = []
    
    # Example pattern for education information (e.g., degree, university)
    education_keywords = ["bachelor's", "master's", "PhD", "degree", "university"]
    
    for keyword in education_keywords:
        if keyword.lower() in resume_text.lower():
            education.append(resume_text.lower().split(keyword)[-1].strip())

    return education
