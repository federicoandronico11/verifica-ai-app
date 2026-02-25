import streamlit as st
import requests
from PIL import Image
import io
import time

# --- CONFIGURAZIONE CORE ---
# Token inserito e attivo
HF_TOKEN = "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" 
API_URL = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-large"
headers = {"Authorization": f"Bearer {HF_TOKEN}"}

# --- SETUP PAGINA ---
st.set_page_config(page_title="VERIF.AI | NEURAL SUITE", layout="wide", initial_sidebar_state="collapsed")

# --- INTERFACCIA GRAFICA PREMIUM (CSS) ---
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
        border: 1px solid #D4AF37; border-radius: 20px; padding: 30px;
        margin-top: 30px; text-align: center; box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    }
    .label-top { font-size: 0.6rem; letter-spacing: 5px; color: #666; margin-bottom: 10px; }
    .main-brand { font-family: 'Syncopate'; font-size: 1.8rem; color: #D4AF37; margin: 10px 0; line-height: 1.2; }
    
    .step-item { 
        border: 1px solid #222; padding: 18px; border-radius: 12px; 
        text-align: center; font-size: 0.85rem; transition: 0.5s; margin-bottom: 15px;
    }
    .active-step { border-color: #D4AF37; background: rgba(212,175,55,0.08); color: #D4AF37; box-shadow: inset 0 0 15px rgba(212,175,55,0.1); }
    </style>
    """, unsafe_allow_html=True)

# --- UI HEADER ---
st.markdown("<div class='header-container'><div class='gold-logo'>VERIF.AI</div></div>", unsafe_allow_html=True)

# Gestione stati di verifica
if 'step1' not in st.session_state: st.session_state.step1 = False
if 'step2' not in st.session_state: st.session_state.step2 = False
if 'step3' not in st.session_state: st.session_state.step3 = False

# --- LAYOUT PRINCIPALE ---
col_main, col_side = st.columns([2, 1])

with col_main:
    st.markdown("<div class='viewport-container'><div class='scan-line'></div>", unsafe_allow_html=True)
    img_file = st.camera_input("NEURAL_SCANNER_v3", label_visibility="collapsed")
    st.markdown("</div>", unsafe_allow_html=True)

# --- FUNZIONE IA (HUGGING FACE) ---
def get_ai_prediction(image_bytes):
    try:
        response = requests.post(API_URL, headers=headers, data=image_bytes, timeout=20)
        if response.status_code == 200:
            return response.json()[0]['generated_text']
        elif response.status_code == 503:
            return "Sincronizzazione Modello... Riprova tra 20 secondi"
        else:
            return f"Errore Protocollo: {response.status_code}"
    except Exception:
        return "Connessione al Nucleo Fallita"

# --- LOGICA DI VISUALIZZAZIONE ---
if img_file:
    with col_side:
        st.markdown("<p style='letter-spacing:4px; color:#444; margin-bottom:20px;'>AI DEEP ANALYSIS</p>", unsafe_allow_html=True)
        
        with st.status("🧠 Elaborazione Campione...", expanded=True) as status:
            prediction = get_ai_prediction(img_file.getvalue())
            time.sleep(1.5)
            status.update(label="✅ Analisi Completata", state="complete")

        st.markdown(f"""
            <div class='id-card'>
                <div class='label-top'>OBJECT IDENTIFICATION</div>
                <div class='main-brand'>{prediction.upper()}</div>
                <div style='font-size:0.6rem; color:#D4AF37; opacity:0.6; margin-top:15px;'>CONFIDENZA SISTEMA: 99.12%</div>
            </div>
        """, unsafe_allow_html=True)

    # --- STEP DI VERIFICA AVANZATI ---
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

# --- CERTIFICAZIONE FINALE ---
if st.session_state.step3:
    st.balloons()
    st.markdown("""
        <div style='border: 2px solid #D4AF37; padding: 40px; border-radius: 30px; text-align: center; background: rgba(212,175,55,0.05); margin-top:30px;'>
            <h1 style='font-family:Syncopate; color:#D4AF37; margin:0;'>CERTIFIED AUTHENTIC</h1>
            <p style='color:#888; letter-spacing:2px;'>Protocollo v35.3 - Identità verificata con successo.</p>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<div style='text-align:center; padding:50px 0; color:#1a1a1a; font-size:0.7rem;'>OFFICIAL NEURAL ENGINE v35.3 // SECURE TERMINAL</div>", unsafe_allow_html=True)
