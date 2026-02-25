import streamlit as st
from PIL import Image
import google.generativeai as genai

# Configura la tua chiave API (assicurati che sia tra le virgolette)
genai.configure(api_key="AIzaSyDboGqQMSa3YTdeQhLK5M7L2AewOnUmrRA") 

model = genai.GenerativeModel('gemini-1.5-flash')

# Interfaccia VERIF.AI
st.markdown("<h1 style='color: #D4AF37;'>📀 VERIF.AI | Scanner Prototipo</h1>", unsafe_allow_html=True)
st.write("Inquadra l'oggetto di lusso e scatta per l'analisi di autenticità.")

img_file_buffer = st.camera_input("Scannerizza Oggetto")

if img_file_buffer is not None:
    img = Image.open(img_file_buffer)
    with st.spinner('Analisi AI in corso...'):
        prompt = "Identifica marca e modello dell'oggetto. Analizza i dettagli e valuta se sembrano autentici. Dai un Trust Score da 0 a 100."
        response = model.generate_content([prompt, img])
        st.subheader("Risultato VERIF.AI:")
        st.success(response.text)
