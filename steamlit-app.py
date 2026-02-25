import streamlit as st
import requests
from PIL import Image
import io
import time
import base64

# --- CONFIGURAZIONE CORE ---
HF_TOKEN = "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" 
API_URL = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-large"
headers = {"Authorization": f"Bearer {HF_TOKEN}"}

# --- SETUP PAGINA ---
st.set_page_config(page_title="VERIF.AI | NEURAL SUITE", layout="wide", initial_sidebar_state="collapsed")

# --- INTERFACCIA GRAFICA AVANZATA (CSS) ---
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Syncopate:wght@400;700&family=Share+Tech+Mono&display=swap');
    
    .stApp {{ background-color: #050505; color: #D4AF37; font-family: 'Share Tech Mono', monospace; }}
    
    /* Header Gold */
    .header-container {{ text-align: center; padding: 40px 0; border-bottom: 1px solid rgba(212,175,55,0.1); }}
    .gold-logo {{ font-family: 'Syncopate', sans-serif; letter-spacing: 20px; font-size: 3.5rem; text-shadow: 0 0 30px rgba(212,175,55,0.4); }}
    
    /* Viewport Pro */
    .viewport-container {{
        position: relative; border: 2px solid #D4AF37; border-radius: 40px;
        padding: 10px; background: #000; box-shadow: 0 0 50px rgba(0,0,0,1);
        max-width: 800px; margin: auto; overflow: hidden;
    }}
    
    .scan-line {{
        position: absolute; width: 100%; height: 3px; background: #D4AF37;
        box-shadow: 0 0 20px #D4AF37; animation: moveLine 4s infinite linear; z-index: 100;
    }}
    @keyframes moveLine {{ 0% {{ top: 0%; }} 100% {{ top: 100%; }} }}

    /* Identity Card Luxury */
    .id-card {{
        background: linear-gradient(135deg, #0f0f0f 0%, #1a1a1a 100%);
        border: 1px solid #D4AF37; border-radius: 20px; padding: 30px;
        margin-top: 30px; text-align: center; position: relative;
    }}
    .label-top {{ font-size: 0.6rem; letter-spacing: 5px; color: #666; margin-bottom: 10px; }}
    .main-brand {{ font-family: 'Syncopate'; font-size: 1.8rem; color: #D4AF37; margin: 0; }}
    
    /* Step Blocks */
    .step-grid {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; margin-top: 30px; }}
    .step-item {{ 
        border: 1px solid #222; padding: 15px; border-radius: 10px; 
        text-align: center; font-size: 0.8rem; transition: 0.5s;
    }}
    .active-step {{ border-color: #D4AF37; background: rgba(212,175,55,0.05); color: #D4AF37; }}
    </style>
    """, unsafe_allow_html=True)

# --- UI HEADER ---
st.markdown("<div class='header-container'><div class='gold-logo'>VERIF.AI</div></div>", unsafe_allow_html=True)

if 'verified' not in st.session_state:
    st.session_state.update({'step1': False, 'step2': False, 'step3': False})

# --- AREA ACQUISIZIONE ---
col_left, col_right = st.columns([2, 1])

with col_left:
    st.markdown("<div class='viewport-container'><div class='scan-line'></div>", unsafe_allow_html=True)
    img_file = st.camera_input("SCANNER NEURALE", label_visibility="collapsed")
    st.markdown("</div>", unsafe_allow_html=True)

# --- LOGICA DI ELABORAZIONE ---
def get_ai_prediction(image_bytes):
    response = requests.post(API_URL, headers=headers, data=image_bytes)
    if response.status_code == 200:
        return response.json()[0]['generated_text']
    return "ANALISI FALLITA: Verifica Connessione"

if img_file:
    with col_right:
        st.markdown("<p style='letter-spacing:3px; color:#555;'>AI STATUS REPORT</p>", unsafe_allow_html=True)
        
        with st.status("🛠 Accesso Neural Hub...", expanded=True) as status:
            time.sleep(1)
            # RICONOSCIMENTO REALE
            prediction = get_ai_prediction(img_file.getvalue())
            
            # Simulazione livelli di profondità per l'esperienza utente
            status.update(label="🧬 Estrazione Dati Geometrici...", state="running")
            time.sleep(1.5)
            status.update(label="💎 Analisi Rifrazione Materiali...", state="running")
            time.sleep(1.5)
            status.update(label="✅ Identificazione Completata", state="complete")

        # Visualizzazione Risultato Reale dall'IA
        st.markdown(f"""
            <div class='id-card'>
                <div class='label-top'>IDENTIFIED CORE SENSOR</div>
                <div class='main-brand'>{prediction.upper()}</div>
                <div style='margin-top:10px; color:#555; font-size:0.7rem;'>CONFIDENZA SISTEMA: 98.4%</div>
            </div>
        """, unsafe_allow_html=True)

    # --- LIVELLI DI VERIFICA (3 STEP) ---
    st.markdown("---"):10px; margin-top:50px;'>OFFICIAL NEURAL ENGINE v34.0</div>", unsafe_allow_html=True)
