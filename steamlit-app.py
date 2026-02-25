import streamlit as st
from PIL import Image
import google.generativeai as genai

# 1. Configurazione API (Usa la tua chiave aggiornata)
genai.configure(api_key="AIzaSyCHgZssMgNI-8XpnN27PXiar-w7eBjnlHU") 

# 2. Inizializzazione Modello con nome standard
model = genai.GenerativeModel('gemini-pro-vision') # Nome ultra-compatibile

st.markdown("<h1 style='color: #D4AF37;'>📀 VERIF.AI | Scanner Live</h1>", unsafe_allow_html=True)

img_file_buffer = st.camera_input("Inquadra l'oggetto")

if img_file_buffer is not None:
    img = Image.open(img_file_buffer)
    
    with st.spinner('Analisi dei materiali e dei loghi in corso...'):
        try:
            # Prompt ottimizzato
            prompt = "Agisci come un esperto di autenticazione. Identifica l'oggetto e dai un Trust Score da 0 a 100."
            
            # Invio all'AI
            response = model.generate_content([prompt, img])
            
            st.subheader("Verdetto VERIF.AI:")
            st.success(response.text)
            
        except Exception as e:
            # Se il modello sopra fallisce, prova il backup (1.5-flash)
            try:
                backup_model = genai.GenerativeModel('gemini-1.5-flash')
                response = backup_model.generate_content([prompt, img])
                st.subheader("Verdetto VERIF.AI (Backup):")
                st.success(response.text)
            except:
                st.error(f"Si è verificato un errore: {e}")
