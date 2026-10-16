import os
import streamlit as st
from google import genai

st.set_page_config(page_title="Meine KI App", page_icon="✨", layout="centered")
st.title("Meine Gemini App")

client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

user_input = st.text_area("Deine Eingabe:", placeholder="Frag etwas...")

if st.button("Absenden", type="primary"):
    if user_input.strip():
        with st.spinner("Antwort wird generiert..."):
            response = client.models.generate_content(
                model="gemini-2.0-flash",
                contents=user_input,
            )
            st.markdown("### Antwort:")
            st.write(response.text)
    else:
        st.warning("Bitte gib zuerst einen Text ein.")
