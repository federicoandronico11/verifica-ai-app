import streamlit as st

def apply_luxury_theme():
    """Applica un design da software ultra-costoso (~150 righe di CSS e logica)."""
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Syncopate:wght@700&family=Inter:wght@400;700&display=swap');
        
        /* Sfondo e Testo Generale */
        .stApp { background-color: #000000; color: #FFFFFF; font-family: 'Inter', sans-serif; }
        
        /* Intestazione Oro */
        .main-title { font-family: 'Syncopate'; color: #D4AF37; letter-spacing: 10px; text-shadow: 0px 0px 15px rgba(212,175,55,0.3); }
        
        /* Pannelli Laterali */
        .side-panel { 
            background: linear-gradient(145deg, #0f0f0f, #1a1a1a);
            border: 1px solid #333;
            border-left: 5px solid #D4AF37;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 10px 10px 20px #050505;
        }
        
        /* Badge Risultati */
        .result-card {
            background: rgba(255, 255, 255, 0.03);
            border-radius: 8px;
            padding: 15px;
            margin-bottom: 20px;
            border-bottom: 1px solid #222;
        }
        
        .label { color: #666; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 2px; }
        .value { color: #D4AF37; font-family: 'Syncopate'; font-size: 1.1rem; }
        </style>
    """, unsafe_allow_html=True)

def render_header():
    st.markdown("<h1 class='main-title' style='text-align:center;'>VERIF.AI</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#444; font-size:0.7rem;'>GLOBAL AUTHENTICATION NODE v88.0</p>", unsafe_allow_html=True)
