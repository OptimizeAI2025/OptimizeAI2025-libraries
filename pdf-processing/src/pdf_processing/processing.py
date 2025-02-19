# pdf_processing module

class PDFProcessor:
    """A simple PDF processor class."""

    def __init__(self, pdf_path):
        self.pdf_path = pdf_path

    def extract_text(self):
        """Fake function that returns sample text from a PDF."""
        return f"Extracted text from {self.pdf_path}"

def extract_text_from_pdf(pdf_path):
    """Standalone function to extract text from a PDF."""
    processor = PDFProcessor(pdf_path)
    return processor.extract_text()
