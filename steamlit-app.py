import streamlit as st
from core_logic import VerifAiCore
import plotly.graph_objects as go

# Configurazione Sistema
API_KEY = "AIzaSyDFVg2nb57u02SmuVq76Sy2q157a0lkJl0"

st.set_page_config(page_title="VERIF.AI TITAN", layout="wide")

# CSS Professionale Carbon & Gold
st.markdown("""
    <style>
    .stApp { background-color: #050505; color: white; font-family: sans-serif; }
    .side-panel { background: #111; padding: 20px; border-left: 4px solid #D4AF37; border-radius: 10px; }
    .gold-label { color: #D4AF37; font-weight: bold; font-size: 1.2rem; margin-bottom: 10px; }
    .sub-text { color: #666; font-size: 0.8rem; text-transform: uppercase; }
    </style>
""", unsafe_allow_html=True)

st.title("🛡️ VERIF.AI | GLOBAL TERMINAL")

# Inizializzazione Motore
core = VerifAiCore(API_KEY)

col_scanner, col_data = st.columns([2, 1], gap="large")

with col_scanner:
    st.subheader("📷 NEURAL SCANNER")
    cam_file = st.camera_input("SCAN", label_visibility="collapsed")
    if cam_file:
        st.image(cam_file, use_container_width=True)

with col_data:
    st.markdown("<div class='side-panel'>", unsafe_allow_html=True)
    st.subheader("📊 ANALYTICS")
    
    if cam_file:
        with st.spinner("Analisi in corso..."):
            res = core.analyze_object(cam_file)
        
        # RISULTATI NELLA TENDINA (IMPECCABILI)
        st.markdown("<p class='sub-text'>Categoria</p>", unsafe_allow_html=True)
        st.markdown(f"<p class='gold-label'>{res['category']}</p>", unsafe_allow_html=True)
        
        st.markdown("<p class='sub-text'>Identified Brand</p>", unsafe_allow_html=True)
        st.markdown(f"<p class='gold-label'>{res['brand']}</p>", unsafe_allow_html=True)
        
        st.markdown("<p class='sub-text'>Model & Revision</p>", unsafe_allow_html=True)
        st.markdown(f"<p class='gold-label'>{res['model']}</p>", unsafe_allow_html=True)
        
        # Gauge Chart
        fig = go.Figure(go.Indicator(
            mode = "gauge+number",
            value = res['confidence'],
            gauge = {'bar': {'color': "#D4AF37"}, 'axis': {'range': [0, 100]}, 'bgcolor': "#000"}
        ))
        fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', font={'color': "white"}, height=200)
        st.plotly_chart(fig, use_container_width=True)
        
        st.success(f"VERDETTO: {res['verdict']}")
    else:
        st.info("Inquadra un oggetto per iniziare.")
    st.markdown("</div>", unsafe_allow_html=True)
