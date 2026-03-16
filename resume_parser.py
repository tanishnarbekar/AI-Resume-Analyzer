import re

def extract_text(filepath, ext):
    """Extract text from PDF, DOCX, or TXT files."""
    if ext == 'pdf':
        return extract_from_pdf(filepath)
    elif ext == 'docx':
        return extract_from_docx(filepath)
    elif ext == 'txt':
        return extract_from_txt(filepath)
    else:
        raise ValueError(f"Unsupported file type: {ext}")

def extract_from_pdf(filepath):
    try:
        from PyPDF2 import PdfReader
        reader = PdfReader(filepath)
        text = ""
        for page in reader.pages:
            extracted = page.extract_text()
            if extracted:
                text += extracted + "\n"
        return text.strip()
    except ImportError:
        raise ImportError("PyPDF2 not installed. Run: pip install PyPDF2")

def extract_from_docx(filepath):
    try:
        import docx
        doc = docx.Document(filepath)
        text = "\n".join([para.text for para in doc.paragraphs])
        return text.strip()
    except ImportError:
        raise ImportError("python-docx not installed. Run: pip install python-docx")

def extract_from_txt(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        return f.read().strip()

def extract_email(text):
    match = re.search(r'[\w\.-]+@[\w\.-]+\.\w+', text)
    return match.group(0) if match else None

def extract_phone(text):
    match = re.search(r'(\+?\d[\d\s\-]{8,14}\d)', text)
    return match.group(0).strip() if match else None

def extract_name(text):
    lines = [l.strip() for l in text.split('\n') if l.strip()]
    return lines[0] if lines else "Unknown"

def get_keyword_density(text, keywords):
    """Count how many times each keyword appears."""
    text_lower = text.lower()
    density = {}
    for kw in keywords:
        count = len(re.findall(r'\b' + re.escape(kw.lower()) + r'\b', text_lower))
        if count > 0:
            density[kw] = count
    return density
