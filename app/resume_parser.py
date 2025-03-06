from PyPDF2 import PdfReader


def extract_text_from_pdf(pdf_file):
    """Extracts text from a PDF file."""
    try:
        # Open the PDF file
        reader = PdfReader(pdf_file)

        # Extract text from all pages
        text = " ".join(
            [page.extract_text() for page in reader.pages if page.extract_text(

            )]
            )

        # Return extracted text
        return text

    except Exception as e:
        # Handle any exceptions (e.g., file not found, invalid PDF)
        return f"Error extracting text: {str(e)}"
