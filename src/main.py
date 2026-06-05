import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from ai_client import get_next_questions, generate_document
from document import save_document


def run():
    print("\n====================================")
    print("       Bienvenida a DocFlow")
    print("====================================\n")

    print("Describe el proceso que quieres documentar.")
    print("Puedes escribir tanto como quieras.\n")
    description = input(">>> ").strip()

    if not description:
        print("No escribiste ninguna descripción. Saliendo.")
        return

    process_name = input("\n¿Cómo se llama este proceso? >>> ").strip()
    if not process_name:
        process_name = "proceso_sin_nombre"

    conversation = []
    round_number = 1

    print("\nDocFlow está analizando tu descripción...\n")

    while True:
        response = get_next_questions(description, conversation)

        if response.strip().upper() == "LISTO":
            print("\n✓ DocFlow tiene suficiente información.")
            print("Generando documento...\n")
            break

        print(f"--- Ronda {round_number} de preguntas ---\n")
        print(response)
        print()

        questions = [
            line.strip() for line in response.split("\n")
            if line.strip() and line.strip()[0].isdigit()
        ]

        if not questions:
            print("Generando documento...\n")
            break

        answers_this_round = []
        for question in questions:
            print(f"{question}")
            print("(escribe /generar para generar el documento ahora)")
            answer = input("Tu respuesta: >>> ").strip()
            
            if answer.lower() == "/generar":
                print("\n✓ Generando documento con la información actual...\n")
                conversation.extend(answers_this_round)
                document = generate_document(description, conversation)
                filename = save_document(document, process_name)
                print("====================================")
                print(f"✓ Documento guardado en: {filename}")
                print("====================================\n")
                print(document)
                return

            answers_this_round.append({
                "question": question,
                "answer": answer
            })
            print()

        conversation.extend(answers_this_round)
        round_number += 1
        print("DocFlow está analizando tus respuestas...\n")

    document = generate_document(description, conversation)

    filename = save_document(document, process_name)

    print("====================================")
    print(f"✓ Documento guardado en: {filename}")
    print("====================================\n")
    print(document)


if __name__ == "__main__":
    run()