import streamlit as st
from PIL import Image
import google.generativeai as genai

# 1. Inserisci qui la tua API Key aggiornata
genai.configure(api_key="AIzaSyCHgZssMgNI-8XpnN27PXiar-w7eBjnlHU")

# 2. Selezione del modello più recente e performante
model = genai.GenerativeModel('gemini-1.5-flash')

st.markdown("<h1 style='color: #D4AF37;'>📀 VERIF.AI | Scanner Live</h1>", unsafe_allow_html=True)
st.write("Inquadra l'oggetto di lusso e scatta per l'analisi.")

img_file_buffer = st.camera_input("Scansiona Oggetto")

if img_file_buffer is not None:
    # Preparazione immagine
    img = Image.open(img_file_buffer)
    
    with st.spinner('Analisi AI in corso...'):
        try:
            # Nuova sintassi per l'invio sicuro di testo + immagine
            response = model.generate_content([
                "Agisci come un esperto mondiale di autenticazione. "
                "Identifica l'oggetto, analizza loghi e materiali e "
                "fornisci un Trust Score da 0 a 100 con una breve spiegazione.", 
                img
            ])
            
            st.subheader("Risultato VERIF.AI:")
            st.success(response.text)
            
        except Exception as e:
            st.error(f"Si è verificato un errore tecnico: {e}")
            st.info("Suggerimento: Verifica che la tua API Key sia attiva su Google AI Studio.")
