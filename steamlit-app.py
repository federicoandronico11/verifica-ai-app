import streamlit as st
from core_logic import VerifAiCore
from branding_assets import apply_luxury_theme, render_header
import plotly.graph_objects as go

# TUA API KEY
API_KEY = "AIzaSyDFVg2nb57u02SmuVq76Sy2q157a0lkJl0"

st.set_page_config(page_title="VERIF.AI", layout="wide")
apply_luxury_theme()
render_header()

core = VerifAiCore(API_KEY)

c1, c2 = st.columns([1.8, 1.2], gap="large")

with c1:
    st.markdown("### 📡 NEURAL SCAN")
    img = st.camera_input("CAPTURE", label_visibility="collapsed")
    if img:
        st.image(img, use_container_width=True)

with c2:
    st.markdown("<div class='side-panel'>", unsafe_allow_html=True)
    st.markdown("### 📊 ANALYTICS")
    
    if img:
        with st.spinner("Decriptazione dati..."):
            res = core.analyze_object(img)
            
        # Visualizzazione Strutturata
        for key in ['category', 'brand', 'model']:
            st.markdown(f"""
                <div class='result-card'>
                    <div class='label'>{key.replace('_', ' ')}</div>
                    <div class='value'>{res.get(key, 'N/A')}</div>
                </div>
            """, unsafe_allow_html=True)
            
        # Gauge
        fig = go.Figure(go.Indicator(
            mode = "gauge+number",
            value = res.get('confidence', 0),
            gauge = {'bar': {'color': "#D4AF37"}, 'axis': {'range': [0, 100]}, 'bgcolor': "#000"}
        ))
        fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', font={'color': "white"}, height=150)
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("Scanner in attesa di segnale...")
    st.markdown("</div>", unsafe_allow_html=True)
