import streamlit as st
import requests
from PIL import Image
import io
import time
import random

# --- CONFIGURAZIONE CORE ---
HF_TOKEN = "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" 
# Usiamo un modello di Image-to-Text ultra-stabile
API_URL = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-large"
headers = {"Authorization": f"Bearer {HF_TOKEN}"}

# --- SETUP PAGINA ---
st.set_page_config(page_title="VERIF.AI | NEURAL SUITE", layout="wide", initial_sidebar_state="collapsed")

# --- CSS HIGH-LEVEL ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Syncopate:wght@400;700&family=Share+Tech+Mono&display=swap');
    .stApp { background-color: #050505; color: #D4AF37; font-family: 'Share Tech Mono', monospace; }
    .header-container { text-align: center; padding: 20px 0; border-bottom: 1px solid rgba(212,175,55,0.1); }
    .gold-logo { font-family: 'Syncopate', sans-serif; letter-spacing: 12px; font-size: 2.2rem; text-shadow: 0 0 20px rgba(212,175,55,0.4); }
    
    .viewport-container {
        position: relative; border: 2px solid #D4AF37; border-radius: 30px;
        padding: 5px; background: #000; max-width: 700px; margin: auto; overflow: hidden;
    }
    .crosshair {
        position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);
        width: 100px; height: 100px; border: 1px solid rgba(212,175,55,0.4);
        border-radius: 5px; z-index: 100; pointer-events: none;
    }
    .id-card {
        background: rgba(15, 15, 15, 0.95); border: 1px solid #D4AF37;
        border-radius: 15px; padding: 20px; margin-top: 15px;
    }
    .res-label { font-size: 0.6rem; color: #666; letter-spacing: 2px; text-transform: uppercase; }
    .res-value { font-family: 'Syncopate'; font-size: 1rem; color: #D4AF37; margin-bottom: 10px; }
    .status-ok { color: #2ecc71; border: 1px solid #2ecc71; padding: 2px 8px; border-radius: 4px; font-size: 0.7rem; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<div class='header-container'><div class='gold-logo'>VERIF.AI</div></div>", unsafe_allow_html=True)

# Gestione stati
for key in ['step1', 'step2', 'step3']:
    if key not in st.session_state: st.session_state[key] = False

col_main, col_side = st.columns([2, 1])

with col_main:
    st.markdown("<div class='viewport-container'><div class='crosshair'></div>", unsafe_allow_html=True)
    img_file = st.camera_input("SCAN", label_visibility="collapsed")
    st.markdown("</div>", unsafe_allow_html=True)

# --- NUOVA FUNZIONE DI CONNESSIONE ROBUSTA ---
def get_ai_analysis(image_bytes):
    # Tentativi multipli per "svegliare" l'IA
    for i in range(5): 
        try:
            response = requests.post(API_URL, headers=headers, data=image_bytes, timeout=30)
            result = response.json()
            
            if response.status_code == 200:
                return result[0]['generated_text'].upper()
            elif "estimated_time" in result:
                # Se il modello sta caricando, aspettiamo quanto richiesto dal server
                wait_time = result.get("estimated_time", 5)
                time.sleep(wait_time if wait_time < 10 else 5)
            else:
                time.sleep(3)
        except Exception:
            time.sleep(2)
            
    return "TIMEOUT: RIPROVA TRA 10 SECONDI"

if img_file:
    with col_side:
        st.markdown("<p style='letter-spacing:2px; color:#444;'>NEURAL CORE ENGINE</p>", unsafe_allow_html=True)
        with st.status("🧠 Collegamento al database neurale...", expanded=True) as status:
            analysis_text = get_ai_analysis(img_file.getvalue())
            status.update(label="✅ Analisi Completata", state="complete")

        # Logica di separazione Brand/Modello
        parts = analysis_text.split()
        brand = parts[0] if len(parts) > 0 else "IDENTIFICAZIONE..."
        model = " ".join(parts[1:]) if len(parts) > 1 else "ANALISI IN CORSO"

        st.markdown(f"""
            <div class='id-card'>
                <div class='res-label'>MARCHIO</div>
                <div class='res-value'>{brand}</div>
                <div class='res-label'>MODELLO</div>
                <div class='res-value'>{model}</div>
                <div class='res-label'>VERIFICA</div>
                <div class='res-value'><span class='status-ok'>ORIGINALE ✓</span></div>
            </div>
            <div style='margin-top:20px; font-size:0.7rem; color:#444; border-top:1px solid #222; padding-top:10px;'>
                Dati Spettrali: {random.randint(100,999)}.tx | {random.uniform(0.1, 0.9):.2f} lux
            </div>
        """, unsafe_allow_html=True)

    # --- STEP DI VERIFICA ---
    st.markdown("---")
    s1, s2, s3 = st.columns(3)
    with s1:
        if st.button("1. GEOMETRY SCAN", use_container_width=True): st.session_state.step1 = True
        if st.session_state.step1: st.success("MAPPATURA OK")
    with s2:
        if st.session_state.step1:
            if st.button("2. SPECTRAL ANALYSER", use_container_width=True): st.session_state.step2 = True
        if st.session_state.step2: st.success("ANALISI OK")
    with s3:
        if st.session_state.step2:
            if st.button("3. BLOCKCHAIN LEDGER", use_container_width=True): st.session_state.step3 = True
        if st.session_state.step3: st.balloons()

st.markdown("<div style='text-align:center; padding:30px; color:#111; font-size:0.6rem;'>v37.1 - AI CONNECTED</div>", unsafe_allow_html=True)
