import pdfplumber
import docx

def extract_text_from_file(path: str) -> str:
    if path.lower().endswith('.pdf'):
        text=''
        with pdfplumber.open(path) as pdf:
            for p in pdf.pages:
                text += p.extract_text() or ''
        return text
    if path.lower().endswith('.docx'):
        d=docx.Document(path)
        return "\n".join([p.text for p in d.paragraphs])
    with open(path,'r',errors='ignore') as f:
        return f.read()
