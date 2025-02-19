import pytest
from pdf_processing import extract_text_from_pdf, PDFProcessor

def test_extract_text_from_pdf():
    assert extract_text_from_pdf("sample.pdf") == "Extracted text from sample.pdf"

def test_pdf_processor():
    processor = PDFProcessor("document.pdf")
    assert processor.extract_text() == "Extracted text from document.pdf"
