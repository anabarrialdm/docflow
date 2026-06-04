import os
from datetime import datetime


def save_document(content: str, process_name: str) -> str:
    os.makedirs("output", exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    clean_name = process_name.lower().replace(" ", "_")
    filename = f"output/{clean_name}_{timestamp}.md"
    
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    
    return filename