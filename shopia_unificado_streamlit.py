
# === SHOPIA UNIFICADO ===

# === backend integrado con Streamlit (no requiere FastAPI por separado) ===

import streamlit as st
import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="ShopIA - Generador de Publicidad", layout="centered")
st.title("🧠 ShopIA - Generador IA de Contenido Publicitario")
st.markdown("Genera imágenes y textos publicitarios para redes sociales con IA.")

with st.form("form_generador"):
    producto = st.text_input("Nombre del producto", max_chars=100)
    objetivo = st.text_area("¿Qué quieres comunicar?", height=100)
    estilo = st.selectbox("Estilo del anuncio", ["emocional", "divertido", "elegante", "directo"])
    submitted = st.form_submit_button("Generar contenido")

if submitted:
    with st.spinner("Generando contenido con IA..."):

        prompt = f'''
        Escribe un texto publicitario profesional para redes sociales sobre el producto "{producto}".
        El objetivo de la publicación es: {objetivo}.
        El estilo debe ser {estilo}. El texto debe incluir:
        - Título atractivo
        - Cuerpo persuasivo
        - Llamado a la acción (CTA)
        - Hashtags relevantes
        '''

        completion = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}]
        )

        texto = completion.choices[0].message.content

        imagen = openai.Image.create(
            prompt=f"Imagen publicitaria profesional de {producto} con estilo {estilo}, fondo limpio, alta calidad, 1080x1350",
            n=1,
            size="1024x1024"
        )

        imagen_url = imagen['data'][0]['url']

        st.subheader("📸 Imagen generada:")
        st.image(imagen_url, use_column_width=True)
        st.subheader("✍️ Copy generado:")
        st.code(texto, language="markdown")
        st.success("¡Contenido generado con éxito!")
