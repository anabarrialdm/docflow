import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

import streamlit as st
from ai_client import get_next_questions, generate_document
from document import save_document

st.set_page_config(page_title="DocFlow", page_icon="📄")

st.title("📄 DocFlow")
st.caption("Documentación inteligente de procesos")

# --- Inicializar estado ---
if "stage" not in st.session_state:
    st.session_state.stage = "inicio"
if "description" not in st.session_state:
    st.session_state.description = ""
if "process_name" not in st.session_state:
    st.session_state.process_name = ""
if "conversation" not in st.session_state:
    st.session_state.conversation = []
if "current_questions" not in st.session_state:
    st.session_state.current_questions = []
if "current_answers" not in st.session_state:
    st.session_state.current_answers = []
if "document" not in st.session_state:
    st.session_state.document = ""
if "filename" not in st.session_state:
    st.session_state.filename = ""

# --- Etapa 1: Descripción inicial ---
if st.session_state.stage == "inicio":
    st.subheader("¿Qué proceso quieres documentar?")

    process_name = st.text_input("Nombre del proceso", placeholder="Ej: Registro de cliente nuevo")
    description = st.text_area("Descríbelo brevemente", placeholder="Explica qué es, cómo funciona, quién lo hace...", height=150)

    if st.button("Comenzar", type="primary"):
        if not process_name or not description:
            st.warning("Por favor completa ambos campos.")
        else:
            st.session_state.process_name = process_name
            st.session_state.description = description
            st.session_state.stage = "preguntas"
            st.rerun()

# --- Etapa 2: Preguntas y respuestas ---
elif st.session_state.stage == "preguntas":
    st.subheader(f"Documentando: {st.session_state.process_name}")

    if st.session_state.conversation:
        with st.expander(f"Ver conversación ({len(st.session_state.conversation)} respuestas)"):
            for entry in st.session_state.conversation:
                st.markdown(f"**Pregunta:** {entry['question']}")
                st.markdown(f"**Respuesta:** {entry['answer']}")
                st.divider()

    if not st.session_state.current_questions:
        with st.spinner("DocFlow está analizando..."):
            response = get_next_questions(
                st.session_state.description,
                st.session_state.conversation
            )

        if response.strip().upper() == "LISTO":
            st.session_state.stage = "generando"
            st.rerun()
        else:
            questions = [
                line.strip() for line in response.split("\n")
                if line.strip() and line.strip()[0].isdigit()
            ]
            st.session_state.current_questions = questions
            st.session_state.current_answers = [""] * len(questions)
            st.rerun()

    else:
        st.markdown("Responde las siguientes preguntas:")
        st.divider()

        answers = []
        for i, question in enumerate(st.session_state.current_questions):
            answer = st.text_area(question, key=f"q_{i}", height=80)
            answers.append(answer)

        col1, col2 = st.columns(2)

        with col1:
            if st.button("Siguiente →", type="primary"):
                if any(a.strip() == "" for a in answers):
                    st.warning("Por favor responde todas las preguntas.")
                else:
                    for q, a in zip(st.session_state.current_questions, answers):
                        st.session_state.conversation.append({
                            "question": q,
                            "answer": a
                        })
                    st.session_state.current_questions = []
                    st.session_state.current_answers = []
                    st.rerun()

        with col2:
            if st.button("Generar documento ahora"):
                for q, a in zip(st.session_state.current_questions, answers):
                    if a.strip():
                        st.session_state.conversation.append({
                            "question": q,
                            "answer": a
                        })
                st.session_state.stage = "generando"
                st.rerun()

# --- Etapa 3: Generando documento ---
elif st.session_state.stage == "generando":
    with st.spinner("Generando documento..."):
        document = generate_document(
            st.session_state.description,
            st.session_state.conversation
        )
        filename = save_document(document, st.session_state.process_name)
        st.session_state.document = document
        st.session_state.filename = filename
        st.session_state.stage = "resultado"
        st.rerun()

# --- Etapa 4: Resultado ---
elif st.session_state.stage == "resultado":
    st.success(f"✓ Documento generado y guardado en: {st.session_state.filename}")

    st.divider()

    # --- Editor ---
    st.subheader("📝 Editar documento")
    st.caption("Puedes editar el documento directamente aquí antes de descargarlo.")

    edited_document = st.text_area(
        label="Contenido del documento",
        value=st.session_state.document,
        height=500,
        label_visibility="collapsed"
    )

    col1, col2 = st.columns(2)

    with col1:
        if st.button("💾 Guardar cambios"):
            st.session_state.document = edited_document
            save_document(edited_document, st.session_state.process_name)
            st.success("Cambios guardados.")

    with col2:
        st.download_button(
            label="⬇ Descargar documento",
            data=edited_document,
            file_name=os.path.basename(st.session_state.filename),
            mime="text/markdown"
        )

    st.divider()

    with st.expander("Vista previa del documento"):
        st.markdown(edited_document)

    st.divider()
    if st.button("Documentar otro proceso"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()