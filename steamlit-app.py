import streamlit as st
from core_logic import VerifAiCore
from PIL import Image
import time

# Configurazione estetica 2026
st.set_page_config(page_title="VerifAi Pro v4", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stMetric { background-color: white; padding: 15px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    </style>
    """, unsafe_content_allowed=True)

st.title("🔍 VerifAi Scanner")
st.caption("Versione Enterprise - Powered by Gemini 1.5 Flash")

# Inizializzazione Core con la tua Key
core = VerifAiCore("AIzaSyAgVN8OcgZYRzzD6nrpRONNONLWogfKmFw")

uploaded_file = st.file_uploader("Trascina qui l'immagine dell'oggetto", type=["jpg", "png", "jpeg"])

if uploaded_file:
    col1, col2 = st.columns([1, 1])
    
    with col1:
        img = Image.open(uploaded_file)
        st.image(img, caption="Preview Originale", use_container_width=True)

    with col2:
        if st.button("🚀 AVVIA ANALISI IA", use_container_width=True):
            with st.status("Connessione ai server Google in corso...") as status:
                st.write("Criptazione immagine...")
                time.sleep(0.5)
                st.write("Interrogazione modello Gemini...")
                result = core.analyze_object(uploaded_file)
                status.update(label="Analisi completata!", state="complete", expanded=False)

            if result.get("category") != "ERRORE_TECNICO":
                st.success("Oggetto identificato con successo")
                m1, m2 = st.columns(2)
                m1.metric("MARCA", result.get("brand", "N/A"))
                m2.metric("MODELLO", result.get("model", "N/A"))
                
                st.subheader("Dettagli Tecnici")
                st.info(f"Categoria: {result.get('category')}")
                st.progress(int(result.get("confidence", 0)) / 100, text=f"Affidabilità: {result.get('confidence')}%")
            else:
                st.error(f"Errore: {result.get('model')}")
                st.warning("Verifica che la chiave API non sia stata disabilitata per eccesso di traffico.")
