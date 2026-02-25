import streamlit as st
from core_logic import VerifAiCore
from PIL import Image

# Configurazione Pagina
st.set_page_config(page_title="VerifAi Professional 2026", layout="wide")
st.title("🔍 VerifAi: Scanner Intelligente")

# Inizializzazione Core
core = VerifAiCore()

uploaded_file = st.file_uploader("Carica un'immagine...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    col1, col2 = st.columns(2)
    image = Image.open(uploaded_file)
    
    with col1:
        st.image(image, caption="Immagine caricata", use_container_width=True)
        
    with col2:
        if st.button("AVVIA SCANSIONE"):
            with st.spinner("Analisi in corso sui server Google..."):
                result = core.analyze_object(uploaded_file)
                
                if result.get("category") != "ERRORE_TECNICO":
                    st.success("✅ Scansione Completata!")
                    st.metric("Categoria", result.get("category"))
                    st.metric("Marca", result.get("brand"))
                    st.metric("Modello", result.get("model"))
                    st.progress(int(result.get("confidence", 0)))
                else:
                    st.error(f"Errore: {result.get('model')}")
                    st.info("Consiglio: Controlla che la API Key sia attiva su Google AI Studio.")
