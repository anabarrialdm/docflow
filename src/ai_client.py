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


def get_next_questions(description: str, conversation: list[dict]) -> str:
    history = format_conversation_history(conversation)
    
    prompt = QUESTIONS_PROMPT.format(
        description=description,
        conversation_history=history
    )

    message = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=1000,
        messages=[{"role": "user", "content": prompt}]
    )

    return message.content[0].text.strip()


def generate_document(description: str, conversation: list[dict]) -> str:
    history = format_conversation_history(conversation)

    prompt = DOCUMENT_PROMPT.format(
        description=description,
        conversation_history=history
    )

    message = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=4000,
        messages=[{"role": "user", "content": prompt}]
    )

    return message.content[0].text.strip()