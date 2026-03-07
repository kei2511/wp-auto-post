import pypdf
import sys

def extract_pdf(pdf_path, txt_path):
    reader = pypdf.PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    with open(txt_path, 'w', encoding='utf-8') as f:
        f.write(text)

if __name__ == "__main__":
    extract_pdf(sys.argv[1], sys.argv[2])
