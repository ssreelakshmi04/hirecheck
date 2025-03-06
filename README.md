## Overview
HireCheck is a Streamlit-based web application that analyzes a resume and matches it against a given job description. It provides a match score and feedback to help users optimize their resumes for Applicant Tracking Systems (ATS).

## Features
- Upload a resume in PDF format
- Paste a job description
- Extract text from the resume
- Compare the resume with the job description using an AI-based matching algorithm
- Display a match score and provide feedback

## Installation
### Prerequisites
- Python 3.7+
- Streamlit
  
## File Structure
```
ats-resume-checker/
│-- app.py                 # Main Streamlit application
│-- app/
│   │-- resume_parser.py   # Extracts text from PDF resumes
│   │-- job_matcher.py     # Matches resume text with job description
│-- requirements.txt       # List of dependencies
│-- README.md              # Project documentation
```

## Usage
1. Open the application in a web browser.
2. Upload a resume in PDF format.
3. Paste the job description in the provided text area.
4. Click the "Analyze" button to get a match score and feedback.

## Dependencies
Ensure the following Python libraries are installed:
- `streamlit`
- `PyMuPDF` (for PDF text extraction)
- `scikit-learn` (for text similarity analysis)
- `nltk` (for natural language processing)
