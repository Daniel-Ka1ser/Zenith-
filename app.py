import os
import streamlit as st
from google import genai

# Page Config für mobiles Look & Feel
st.set_page_config(page_title="Meine KI App", page_icon="✨", layout="centered")
st.title("Meine Gemini App")

# API Client initialisieren (unterstützt auch Cloud-/Workspace-Tokens)
api_key = os.environ.get("GEMINI_API_KEY")
if api_key:
    client = genai.Client(api_key=api_key)
else:
    client = genai.Client()

# Einfaches Eingabefeld
user_input = st.text_area("Deine Eingabe:", placeholder="Frag etwas...")

if st.button("Absenden", type="primary"):
    if user_input.strip():
        with st.spinner("Antwort wird generiert..."):
            try:
                # Anfrage an das Gemini 2.0 Flash Modell senden
                response = client.models.generate_content(
                    model="gemini-2.0-flash",
                    contents=user_input,
                )
                st.markdown("### Antwort:")
                st.write(response.text)
            except Exception as e:
                st.error(f"Ein Fehler ist aufgetreten: {e}")
    else:
        st.warning("Bitte gib zuerst einen Text ein.")
