import streamlit as st
from PIL import Image
import google.generativeai as genai

# Configurazione API
genai.configure(api_key="TUA_CHIAVE_API") 
model = genai.GenerativeModel('gemini-1.5-flash')

st.markdown("<h1 style='color: #D4AF37;'>📀 VERIF.AI | Scanner Live</h1>", unsafe_allow_html=True)

img_file_buffer = st.camera_input("Inquadra l'oggetto")

if img_file_buffer is not None:
    # Convertiamo correttamente l'immagine per l'AI
    img = Image.open(img_file_buffer)
    
    with st.spinner('Analisi dei materiali e dei loghi...'):
        try:
            # Usiamo una lista per passare i dati correttamente
            response = model.generate_content([
                "Agisci come un perito esperto di beni di lusso. Identifica l'oggetto nella foto. "
                "Valuta l'autenticità basandoti su loghi, scritte e materiali visibili. "
                "Fornisci un Trust Score da 0 a 100 e giustifica brevemente il voto.", 
                img
            ])
            
            st.subheader("Verdetto VERIF.AI:")
            st.success(response.text)
        except Exception as e:
            st.error(f"Errore durante l'analisi: {e}")
