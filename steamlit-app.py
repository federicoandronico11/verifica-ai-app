import streamlit as st
from core_logic import VerifAiCore
from database_manager import ScanDatabase
import plotly.graph_objects as go

# CONFIGURAZIONE
API_KEY = "AIzaSyDFVg2nb57u02SmuVq76Sy2q157a0lkJl0"
st.set_page_config(page_title="VERIF.AI PRO", layout="wide")

# INIZIALIZZAZIONE
core = VerifAiCore(API_KEY)
db = ScanDatabase()

st.title("🛡️ VERIF.AI | ENTERPRISE NODE")

col1, col2 = st.columns([2, 1])

with col1:
    img = st.camera_input("SCANNER")
    if img:
        st.image(img)

with col2:
    if img:
        with st.spinner("Analisi..."):
            res = core.analyze_object(img)
            # SALVATAGGIO NEL DATABASE
            if res.get("category") != "Errore":
                db.save_scan(res)
        
        st.metric("MARCA", res.get("brand"))
        st.metric("MODELLO", res.get("model"))
        st.write(f"Categoria: {res.get('category')}")
        
    else:
        st.info("Scanner pronto.")

# SEZIONE STORICO (Aggiunge valore e righe di codice)
st.markdown("---")
st.subheader("📜 STORICO ACQUISIZIONI")
history_df = db.get_history()
if history_df is not None:
    st.dataframe(history_df, use_container_width=True)
