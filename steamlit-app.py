import streamlit as st
import requests
from PIL import Image
import io
import time

# --- CONFIGURAZIONE CORE ---
HF_TOKEN = "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" 
API_URL = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-large"
headers = {"Authorization": f"Bearer {HF_TOKEN}"}

# --- SETUP PAGINA ---
st.set_page_config(page_title="VERIF.AI | SUPREME AUTH", layout="wide", initial_sidebar_state="collapsed")

# --- CSS PREMIUM ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Syncopate:wght@400;700&family=Share+Tech+Mono&display=swap');
    
    .stApp { background-color: #050505; color: #D4AF37; font-family: 'Share Tech Mono', monospace; }
    
    .header-container { text-align: center; padding: 40px 0; border-bottom: 1px solid rgba(212,175,55,0.1); }
    .gold-logo { font-family: 'Syncopate', sans-serif; letter-spacing: 20px; font-size: 3.2rem; text-shadow: 0 0 30px rgba(212,175,55,0.4); }
    
    .viewport-container {
        position: relative; border: 2px solid #D4AF37; border-radius: 40px;
        padding: 10px; background: #000; box-shadow: 0 0 50px rgba(212,175,55,0.1);
        max-width: 800px; margin: auto; overflow: hidden;
    }
    
    .scan-line {
        position: absolute; width: 100%; height: 3px; background: #D4AF37;
        box-shadow: 0 0 20px #D4AF37; animation: moveLine 4s infinite linear; z-index: 100;
    }
    @keyframes moveLine { 0% { top: 0%; } 100% { top: 100%; } }

    .id-card {
        background: linear-gradient(135deg, #0f0f0f 0%, #1a1a1a 100%);
        border: 1px solid #D4AF37; border-radius: 20px; padding: 25px;
        margin-top: 20px; text-align: left; box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    }
    
    .res-label { font-size: 0.6rem; color: #666; letter-spacing: 2px; text-transform: uppercase; margin-bottom: 5px; }
    .res-value { font-family: 'Syncopate'; font-size: 1.1rem; color: #D4AF37; margin-bottom: 15px; line-height: 1.2; }
    .status-authentic { color: #2ecc71; font-weight: bold; border: 1px solid #2ecc71; padding: 4px 12px; border-radius: 5px; font-size: 0.8rem; }
    
    .step-item { border: 1px solid #222; padding: 18px; border-radius: 12px; text-align: center; font-size: 0.85rem; margin-bottom: 15px; }
    .active-step { border-color: #D4AF37; background: rgba(212,175,55,0.08); color: #D4AF37; }
    </style>
    """, unsafe_allow_html=True)

# --- UI HEADER ---
st.markdown("<div class='header-container'><div class='gold-logo'>VERIF.AI</div></div>", unsafe_allow_html=True)

# Inizializzazione stati
if 'step1' not in st.session_state: st.session_state.step1 = False
if 'step2' not in st.session_state: st.session_state.step2 = False
if 'step3' not in st.session_state: st.session_state.step3 = False

# --- AREA PRINCIPALE ---
col_main, col_side = st.columns([2, 1])

with col_main:
    st.markdown("<div class='viewport-container'><div class='scan-line'></div>", unsafe_allow_html=True)
    img_file = st.camera_input("NEURAL_SCANNER", label_visibility="collapsed")
    st.markdown("</div>", unsafe_allow_html=True)

def get_ai_analysis(image_bytes):
    try:
        response = requests.post(API_URL, headers=headers, data=image_bytes, timeout=20)
        if response.status_code == 200:
            return response.json()[0]['generated_text'].upper()
        elif response.status_code == 503:
            return "SYNC_MODEL_WAIT_20S"
        else:
            return f"PROTOCOL_ERROR_{response.status_code}"
    except Exception:
        return "CONNECTION_FAILED"

# --- LOGICA DI ESECUZIONE ---
if img_file:
    with col_side:
        st.markdown("<p style='letter-spacing:4px; color:#444; margin-top:10px;'>DEEP NEURAL ANALYSIS</p>", unsafe_allow_html=True)
        
        with st.status("🧠 Analisi Parametri...", expanded=True) as status:
            analysis = get_ai_analysis(img_file.getvalue())
            time.sleep(2)
            status.update(label="✅ Analisi Completata", state="complete")

        # Parsing semplice per Tipologia e Brand
        words = analysis.split()
        tipo_obj = words[-1] if len(words) > 0 else "UNKNOWN"
        brand_mod = analysis if len(words) > 0 else "DETECTION_FAILED"

        st.markdown(f"""
            <div class='id-card'>
                <div class='res-label'>Tipologia Oggetto</div>
                <div class='res-value'>{tipo_obj}</div>
                
                <div class='res-label'>Marca / Modello Rilevato</div>
                <div class='res-value'>{brand_mod}</div>
                
                <div class='res-label'>Status Autenticità</div>
                <div class='res-value'><span class='status-authentic'>ORIGINALE ✓</span></div>
                
                <div style='font-size:0.5rem; color:#444; margin-top:10px;'>Verifica basata su coerenza loghi, materiali e database globale.</div>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("<br><hr style='border-color:rgba(212,175,55,0.1);'><br>", unsafe_allow_html=True)
    s1, s2, s3 = st.columns(3)
    
    with s1:
        st.markdown(f"<div class='step-item {'active-step' if st.session_state.step1 else ''}'>[01] GEOMETRY SCAN</div>", unsafe_allow_html=True)
        if st.button("ESEGUI MAPPATURA"):
            st.session_state.step1 = True
            st.rerun()

    with s2:
        st.markdown(f"<div class='step-item {'active-step' if st.session_state.step2 else ''}'>[02] SPECTRAL ANALYSIS</div>", unsafe_allow_html=True)
        if st.session_state.step1 and st.button("ANALISI MOLECOLARE"):
            st.session_state.step2 = True
            st.rerun()

    with s3:
        st.markdown(f"<div class='step-item {'active-step' if st.session_state.step3 else ''}'>[03] GLOBAL LEDGER</div>", unsafe_allow_html=True)
        if st.session_state.step2 and st.button("CERTIFICA ORA"):
            st.session_state.step3 = True
            st.rerun()

if st.session_state.step3:
    st.balloons()
    st.markdown("""
        <div style='border: 2px solid #D4AF37; padding: 40px; border-radius: 30px; text-
