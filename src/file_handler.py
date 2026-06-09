import os
import fitz  # pymupdf
import docx
from PIL import Image
import base64


def extract_text_from_pdf(file_path: str) -> str:
    doc = fitz.open(file_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text.strip()


def extract_text_from_docx(file_path: str) -> str:
    doc = docx.Document(file_path)
    text = ""
    for paragraph in doc.paragraphs:
        text += paragraph.text + "\n"
    return text.strip()


def extract_text_from_txt(file_path: str) -> str:
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        return f.read().strip()


def image_to_base64(file_path: str) -> str:
    with open(file_path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")


def get_image_media_type(filename: str) -> str:
    ext = filename.lower().split(".")[-1]
    types = {
        "jpg": "image/jpeg",
        "jpeg": "image/jpeg",
        "png": "image/png",
        "gif": "image/gif",
        "webp": "image/webp"
    }
    return types.get(ext, "image/jpeg")


def process_uploaded_file(file_bytes: bytes, filename: str) -> dict:
    ext = filename.lower().split(".")[-1]
    
    import tempfile
    with tempfile.NamedTemporaryFile(suffix=f".{ext}", delete=False) as tmp:
        tmp.write(file_bytes)
        tmp_path = tmp.name

    try:
        if ext == "pdf":
            text = extract_text_from_pdf(tmp_path)
            return {"type": "text", "content": text, "filename": filename}
        
        elif ext == "docx":
            text = extract_text_from_docx(tmp_path)
            return {"type": "text", "content": text, "filename": filename}
        
        elif ext == "txt":
            text = extract_text_from_txt(tmp_path)
            return {"type": "text", "content": text, "filename": filename}
        
        elif ext in ["jpg", "jpeg", "png", "gif", "webp"]:
            b64 = image_to_base64(tmp_path)
            media_type = get_image_media_type(filename)
            return {"type": "image", "content": b64, "media_type": media_type, "filename": filename}
        
        else:
            return {"type": "unsupported", "filename": filename}
    
    finally:
        os.unlink(tmp_path)