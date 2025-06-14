
import streamlit as st
import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="ShopIA - Chatbot IA", layout="centered")
st.title("💬 ShopIA - Simulador de Chatbot con IA")

if "messages" not in st.session_state:
    st.session_state.messages = []

input_usuario = st.text_input("Escribe tu mensaje como si fueras un cliente:", key="user_input")

if st.button("Enviar"):
    if input_usuario:
        st.session_state.messages.append({"role": "user", "content": input_usuario})

        # Enviar a OpenAI
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[{"role": "system", "content": "Eres un asistente amable de una tienda online. Responde de forma útil y breve."}] + st.session_state.messages
        )
        respuesta_ia = response.choices[0].message.content

        st.session_state.messages.append({"role": "assistant", "content": respuesta_ia})

# Mostrar historial
st.subheader("📝 Conversación:")
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"🧍 **Cliente:** {msg['content']}")
    else:
        st.markdown(f"🤖 **ShopIA:** {msg['content']}")
