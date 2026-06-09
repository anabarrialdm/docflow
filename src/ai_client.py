import os
import anthropic
from dotenv import load_dotenv
from prompts import QUESTIONS_PROMPT, DOCUMENT_PROMPT

load_dotenv()

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))


def format_conversation_history(conversation: list[dict]) -> str:
    if not conversation:
        return "Sin conversación previa."
    
    result = ""
    for entry in conversation:
        result += f"Pregunta: {entry['question']}\n"
        result += f"Respuesta: {entry['answer']}\n\n"
    return result


def build_messages_with_files(prompt: str, files: list[dict]) -> list:
    content = []

    for f in files:
        if f["type"] == "image":
            content.append({
                "type": "image",
                "source": {
                    "type": "base64",
                    "media_type": f["media_type"],
                    "data": f["content"]
                }
            })
        elif f["type"] == "text":
            content.append({
                "type": "text",
                "text": f"Contenido del archivo '{f['filename']}':\n\n{f['content']}"
            })

    content.append({"type": "text", "text": prompt})
    return [{"role": "user", "content": content}]


def get_next_questions(description: str, conversation: list[dict], files: list[dict] = []) -> str:
    history = format_conversation_history(conversation)

    prompt = QUESTIONS_PROMPT.format(
        description=description,
        conversation_history=history
    )

    messages = build_messages_with_files(prompt, files) if files else [
        {"role": "user", "content": prompt}
    ]

    message = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=1000,
        messages=messages
    )

    return message.content[0].text.strip()


def generate_document(description: str, conversation: list[dict], files: list[dict] = []) -> str:
    history = format_conversation_history(conversation)

    prompt = DOCUMENT_PROMPT.format(
        description=description,
        conversation_history=history
    )

    messages = build_messages_with_files(prompt, files) if files else [
        {"role": "user", "content": prompt}
    ]

    message = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=4000,
        messages=messages
    )

    return message.content[0].text.strip()