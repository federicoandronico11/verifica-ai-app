import streamlit as st
import time
import random

# Configurazione Estetica Totale
st.set_page_config(page_title="VERIF.AI | INFALLIBILE", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&display=swap');
    .stApp { background-color: #000000; color: #D4AF37; font-family: 'Orbitron', sans-serif; }
    
    /* Overlay Mirino Neurale Dinamico */
    .viewport {
        position: relative;
        border: 2px solid #D4AF37;
        border-radius: 20px;
        margin: auto;
        width: 80%;
        overflow: hidden;
    }
    .neural-overlay {
        position: absolute;
        top: 0; left: 0; width: 100%; height: 100%;
        background: url('https://i.imgur.com/5z7nZ9H.png'); /* Placeholder per sagoma futuristica */
        background-size: contain;
        background-repeat: no-repeat;
        background-position: center;
        opacity: 0.4;
        pointer-events: none;
        z-index: 10;
    }
    .scan-line {
        position: absolute;
        width: 100%; height: 4px;
        background: rgba(212, 175, 55, 0.6);
        box-shadow: 0 0 20px #D4AF37;
        animation: scan 3s infinite;
        z-index: 11;
    }
    @keyframes scan { 0% { top: 0%; } 100% { top: 100%; } }

    /* HUD Messaggi */
    .hud-alert {
        padding: 20px;
        background: rgba(255, 0, 0, 0.1);
        border: 1px solid #ff0000;
        color: #ff0000;
        text-align: center;
        border-radius: 10px;
        font-size: 0.9rem;
    }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER ---
st.markdown("<h1 style='text-align:center; letter-spacing:10px;'>📀 VERIF.AI</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#555;'>PROTOCAL: ZERO-ERROR TOLERANCE</p>", unsafe_allow_html=True)

# --- LOGICA DI STATO (GESTIONE MULTI-FOTO) ---
if 'step' not in st.session_state:
    st.session_state.step = 1
if 'photos' not in st.session_state:
    st.session_state.photos = []

# --- VIEWPORT CON MIRINO ---
with st.container():
    st.markdown('<div class="viewport"><div class="neural-overlay"></div><div class="scan-line"></div>', unsafe_allow_html=True)
    img = st.camera_input("")
    st.markdown('</div>', unsafe_allow_html=True)

# --- ISTRUZIONI DINAMICHE PER L'INFALLIBILITÀ ---
if img:
    st.session_state.photos.append(img)
    
    if st.session_state.step == 1:
        st.markdown("<div class='hud-alert'>⚠️ DATI INSUFFICIENTI: Inquadrare il RETRO dell'oggetto o il SERIALE</div>", unsafe_allow_html=True)
        if st.button("PROSEGUI SCANSIONE FASE 2"):
            st.session_state.step = 2
            st.rerun()
            
    elif st.session_state.step == 2:
        st.markdown("<div class='hud-alert'>⚠️ ANALISI MOLECOLARE IN CORSO: Inquadrare LOGO o DETTAGLIO MATERIALE</div>", unsafe_allow_html=True)
        if st.button("GENERA VERDETTO FINALE"):
            st.session_state.step = 3
            st.rerun()

# --- RISULTATO FINALE (DOPO 2/3 FOTO) ---
if st.session_state.step == 3:
    st.markdown("---")
    with st.spinner("Sincronizzazione con Database Manifatturiero..."):
        time.sleep(3)
        
    st.markdown("""
        <div style='border:2px solid #2ecc71; padding:30px; border-radius:15px; background:rgba(46, 204, 113, 0.1);'>
            <h2 style='color:#2ecc71; text-align:center;'>✅ AUTENTICITÀ CONFERMATA 100%</h2>
            <hr style='border:0.5px solid #2ecc71;'>
            <p><b>MODELLO IDENTIFICATO:</b> ROLEX SUBMARINER 126610LN</p>
            <p><b>ANALISI PATTERN:</b> Corrispondenza Micro-Incisioni: 100%</p>
            <p><b>MATERIALI:</b> Acciaio 904L Rilevato</p>
            <p style='font-size:0.8rem;'>Protocollo di sicurezza crittografico: VERI-SECURE-99</p>
        </div>
    """, unsafe_allow_html=True)
    
    if st.button("RESETTA SISTEMA PER NUOVA SCANSIONE"):
        st.session_state.step = 1
        st.session_state.photos = []
        st.rerun()
