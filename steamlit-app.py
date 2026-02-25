import streamlit as st
from core_logic import VerifAiCore
from PIL import Image
import time

# Configurazione della pagina - Standard 2026
st.set_page_config(page_title="VerifAi Pro v4", layout="wide")

# FIX ERRORE: Il parametro corretto è unsafe_allow_html=True
st.markdown("""
    <style>
    .stApp { background-color: #f8f9fa; }
    .main-card { background-color: white; padding: 20px; border-radius: 15px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
    </style>
    """, unsafe_allow_html=True)

st.title("🔍 VerifAi Scanner")
st.write("Analizzatore Professionale di Oggetti")

# Inizializzazione Core con la tua Key
core = VerifAiCore("AIzaSyAgVN8OcgZYRzzD6nrpRONNONLWogfKmFw")

uploaded_file = st.file_uploader("Carica immagine", type=["jpg", "png", "jpeg"])

if uploaded_file:
    c1, c2 = st.columns(2)
    with c1:
        img = Image.open(uploaded_file)
        st.image(img, use_container_width=True)
    
    with c2:
        if st.button("ESEGUI SCANSIONE", use_container_width=True):
            with st.spinner("IA in ascolto..."):
                res = core.analyze_object(uploaded_file)
                
                if res.get("category") != "ERRORE_TECNICO":
                    st.success("Analisi Completata")
                    st.metric("Marca", res.get("brand", "N/A"))
                    st.metric("Modello", res.get("model", "N/A"))
                    st.info(f"Categoria: {res.get('category')}")
                else:
                    st.error(f"Errore API: {res.get('model')}")
                
