import streamlit as st          st.successge
import google.generativeai as genai

# Configura la tua chiave API qui tra le virgolette
genai.configure(api_key="AIzaSyDboGqQMSa3YTdeQhLK5M7L2Aew0nUmrRA") 

model = genai.GenerativeModel('gemini-1.5-flash')

st.title("📀 VERIF.AI | Scanner Prototipo")
st.write("Inquadra l'oggetto di lusso e scatta per l'analisi.")

img_file_buffer = st.camera_input("Scannerizza Oggetto")

if img_file_buffer is not None:
    img = Image.open(img_file_buffer)
    with st.spinner('Analisi AI in corso...'):
        prompt = "Identifica marca e modello dell'oggetto e valuta se i dettagli sembrano autentici. Dai un Trust Score da 0 a 100."
        response = model.generate_content([prompt, img])
        st.subheader("Risultato VERIF.AI:")
        st.success(response.text)
