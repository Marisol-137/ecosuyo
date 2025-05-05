# frontend/pages/Chat.py

import streamlit as st
import sys
import os

# Agrega la raíz del proyecto al sys.path para permitir imports globales
root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if root_path not in sys.path:
    sys.path.append(root_path)

from langchain_module.model_client import get_llm_response

# Inicializar historial en sesión
if "mensajes" not in st.session_state:
    st.session_state.mensajes = []

st.title("🤖 Chat con IA de IBM Watsonx")

# Muestra historial de conversación estilo burbuja tipo chat
for msg in st.session_state.mensajes:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Caja de entrada del usuario
prompt = st.chat_input("Escribe tu mensaje...")

if prompt:
    # Mostrar mensaje del usuario
    st.chat_message("user").markdown(prompt)
    st.session_state.mensajes.append({"role": "user", "content": prompt})

    # Obtener respuesta de watsonx
    respuesta = get_llm_response(prompt)

    # Mostrar respuesta del modelo
    st.chat_message("assistant").markdown(respuesta)
    st.session_state.mensajes.append({"role": "assistant", "content": respuesta})
