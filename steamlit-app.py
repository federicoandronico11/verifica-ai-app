import streamlit as st
from PIL import Image
import google.generativeai as genai

# Configurazione API
# Assicurati che la chiave sia attiva su Google AI Studio
genai.configure(api_key="AIzaSyBrHsIvD101F1-VoXNlxJjoXXLba-ynHRc")

st.markdown("<h1 style='color: #D4AF37;'>📀 VERIF.AI | Scanner Live</h1>", unsafe_allow_html=True)

img_file_buffer = st.camera_input("Inquadra l'oggetto per l'analisi")

if img_file_buffer is not None:
    img = Image.open(img_file_buffer)
    
    with st.spinner('Analisi in corso...'):
        try:
            # FORZIAMO IL MODELLO FLASH SULLA VERSIONE STABILE
            model = genai.GenerativeModel('models/gemini-1.5-flash')
            
            # Chiamata all'AI
            response = model.generate_content([
                "Agisci come un esperto di autenticazione. Identifica l'oggetto e dai un Trust Score da 0 a 100.", 
                img
            ])
            
            st.subheader("Verdetto VERIF.AI:")
            st.success(response.text)
            
        except Exception as e:
            st.error(f"Errore tecnico: {e}")
            st.info("Se l'errore persiste, controlla che la fatturazione sia abilitata (anche se nel piano gratuito) su Google Cloud Console.")
