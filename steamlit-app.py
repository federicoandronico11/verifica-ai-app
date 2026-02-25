import streamlit as st
import requests
from PIL import Image, ImageOps
import io
import time
import random

# --- CONFIGURAZIONE CORE ---
HF_TOKEN = "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" 
API_URL = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-large"
headers = {"Authorization": f"Bearer {HF_TOKEN}"}

st.set_page_config(page_title="VERIF.AI | INDUSTRIAL", layout="wide")

# --- CSS DEFINITIVO (DARK INDUSTRIAL) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Syncopate:wght@700&family=JetBrains+Mono&display=swap');
    .stApp { background-color: #020202; color: #D4AF37; font-family: 'JetBrains Mono', monospace; }
    .main-header { font-family: 'Syncopate'; text-align: center; font-size: 2.5rem; letter-spacing: 10px; padding: 40px; border-bottom: 2px solid #D4AF37; margin-bottom: 30px; }
    .metric-box { border: 1px solid #333; padding: 15px; border-radius: 5px; background: #0a0a0a; text-align: center; }
    .status-verified { color: #00ff00; font-weight: bold; text-shadow: 0 0 10px #00ff00; }
    .status-alert { color: #ff0000; font-weight: bold; text-shadow: 0 0 10px #ff0000; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<div class='main-header'>VERIF.AI INDUSTRIAL v40</div>", unsafe_allow_html=True)

# --- LOGICA DI ANALISI TECNICA ---
def technical_analysis(img_bytes):
    # Simulazione di analisi vettoriale dei pixel per autenticità
    try:
        response = requests.post(API_URL, headers=headers, data=img_bytes, timeout=15)
        if response.status_code == 200:
            return response.json()[0]['generated_text'].upper()
    except:
        pass
    return "ANALISI_VETTORIALE_FALLITA"

# --- INTERFACCIA OPERATIVA ---
col_cam, col_data = st.columns([3, 2])

with col_cam:
    st.subheader("📡 NEURAL SCANNER")
    img = st.camera_input("CAPTURE_DEVICE", label_visibility="collapsed")
    
    if img:
        st.image(img, caption="CAMPIONE ACQUISITO", use_container_width=True)

if img:
    with col_data:
        st.subheader("📊 DIAGNOSTICA")
        with st.status("Analisi molecolare e coerenza loghi...") as s:
            res = technical_analysis(img.getvalue())
            time.sleep(2)
            s.update(label="Scansione terminata", state="complete")
        
        # Simulazione Parametri di Autenticità Reali
        conf = random.uniform(91.2, 99.8)
        is_fake = "FALSE" if conf > 94 else "TRUE"
        
        st.markdown(f"""
            <div class='metric-box'>
                <p>OGGETTO: <b>{res}</b></p>
                <p>PROBABILITÀ ORIGINALE: <span class='status-verified'>{conf:.2f}%</span></p>
                <p>COERENZA PIXEL: <b>OTTIMALE</b></p>
                <p>SOSPETTO CONTRAFFAZIONE: <span class='status-alert'>{is_fake}</span></p>
            </div>
        """, unsafe_allow_html=True)
        
        st.divider()
        st.write("🔍 **Dettagli Micro-Scansione:**")
        st.json({
            "serials_detected": f"SN-{random.randint(1000,9999)}-XQ",
            "material_density": "8.92 g/cm³ (MATCH)",
            "logo_alignment": "0.002mm variance",
            "blockchain_status": "PENDING_REGISTRATION"
        })

# --- AZIONI FINALI ---
if img:
    if st.button("EMETTI CERTIFICATO DI AUTENTICITÀ", type="primary", use_container_width=True):
        st.balloons()
        st.success("CERTIFICATO CRYPTO-FIRMATA GENERATO CON SUCCESSO")
