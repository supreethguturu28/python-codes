import os
import json
from docx import Document
from tqdm import tqdm


def extract_text_from_docx(file_path):
    try:
        doc = Document(file_path)
        return "\n".join([para.text for para in doc.paragraphs if para.text.strip()])
    except Exception as e:
        return f"[Error reading file: {e}]"


def find_docx_files(folder_path):
    docx_files = []
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith(".docx") and not file.startswith("~$"):
                docx_files.append(os.path.join(root, file))
    return docx_files


def collect_docx_texts(folder_path):
    docx_files = find_docx_files(folder_path)
    docx_texts = {}

    for file_path in tqdm(docx_files, desc="Reading .docx files", unit="file"):
        text = extract_text_from_docx(file_path)
        docx_texts[file_path] = text

    return docx_texts


# Example usage
if __name__ == "__main__":
    folder_path = r"C:\Users\Supreeth\Downloads\Training Overview Word Docs"
    docx_data = collect_docx_texts(folder_path)
    print(json.dumps(docx_data, indent=2, ensure_ascii=False))
