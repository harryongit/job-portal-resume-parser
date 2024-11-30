# utils/pdf_utils.py

import PyPDF2

def extract_text_from_pdf(pdf_file_path):
    """
    Extracts text content from a PDF file.
    :param pdf_file_path: Path to the PDF file
    :return: Extracted text from the PDF
    """
    try:
        with open(pdf_file_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            text = ""
            for page_num in range(len(reader.pages)):
                page = reader.pages[page_num]
                text += page.extract_text()
            return text
    except Exception as e:
        print(f"Error while extracting text from PDF: {e}")
        return None
