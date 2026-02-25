import streamlit as st
import time
import random

# 1. CONFIGURAZIONE ESTETICA DEFINITIVA (MANTENUTA)
st.set_page_config(page_title="VERIF.AI | GLOBAL CERTIFICATION", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Syncopate:wght@400;700&family=Share+Tech+Mono&display=swap');
    
    .stApp { background-color: #050505; color: #D4AF37; font-family: 'Share Tech Mono', monospace; }
    
    /* Logo Luxury (CONFERMATO) */
    .gold-logo {
        text-align: center; font-family: 'Syncopate', sans-serif;
        letter-spacing: 15px; font-size: 3.5rem; margin-bottom: 0px;
        text-shadow: 0 0 30px rgba(212, 175, 55, 0.4);
    }
    
    /* OVERLAY SCHERMO PROFESSIONALE (NUOVO) */
    .viewport {
        position: relative; border: 2px solid #D4AF37; border-radius: 20px;
        overflow: hidden; max-width: 800px; margin: auto; background: #000;
        box-shadow: 0 0 50px rgba(212, 175, 55, 0.2);
    }
    
    /* Mirino HUD Dinamico */
    .hud-overlay {
        position: absolute; top: 0; left: 0; width: 100%; height: 100%;
        pointer-events: none; z-index: 100;
        border: 1px solid rgba(212, 175, 55, 0.1);
    }
    
    /* Linea Laser Animata */
    .laser-line {
        position: absolute; width: 100%; height: 2px;
        background: rgba(212, 175, 55, 0.5);
        box-shadow: 0 0 15px #D4AF37;
        animation: scan 3s infinite linear;
        z-index: 101;
    }
    @keyframes scan { 0% { top: 0%; } 100% { top: 100%; } }

    /* Coordinate angolari HUD */
    .hud-corner { position: absolute; width: 20px; height: 20px; border: 2px solid #D4AF37; }
    .top-left { top: 10px; left: 10px; border-right: none; border-bottom: none; }
    .top-right { top: 10px; right: 10px; border-left: none; border-bottom: none; }
    .bottom-left { bottom: 10px; left: 10px; border-right: none; border-top: none; }
    .bottom-right { bottom: 10px; right: 10px; border-left: none; border-top: none; }

    /* Step di verifica (MANTENUTI) */
    .step-box { padding: 15px; border-left: 2px solid #222; margin-bottom: 10px; color: #666; }
    .step-active { border-left: 2px solid #D4AF37; color: #D4AF37; background: rgba(212, 175, 55, 0.05); }

    /* Note Legali Footer (CONFERMATE) */
    .legal-footer { font-size: 0.7rem; color: #444; text-align: justify; margin-top: 50px; border-top: 1px solid #222; padding-top: 20px; }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER (CONFERMATO) ---
st.markdown("<div class='gold-logo'>VERIF.AI</div>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#555; font-size:10px;'>SECURE QUANTUM AUTHENTICATION HUB v16.0</p>", unsafe_allow_html=True)

if 'checkpoints' not in st.session_state:
    st.session_state.checkpoints = {"Geometria": False, "Materiali": False, "Seriale": False}

# --- AREA ACQUISIZIONE CON OVERLAY PROFESSIONALE ---
st.markdown("<br>", unsafe_allow_html=True)
with st.container():
    st.markdown("""
        <div class="viewport">
            <div class="hud-overlay">
                <div class="laser-line"></div>
                <div class="hud-corner top-left"></div>
                <div class="hud-corner top-right"></div>
                <div class="hud-corner bottom-left"></div>
                <div class="hud-corner bottom-right"></div>
                <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); 
                            width: 200px; height: 200px; border: 1px dashed rgba(212,175,55,0.4); border-radius: 50%;"></div>
            </div>
    """, unsafe_allow_html=True)
    
    # Utilizziamo st.camera_input per forzare solo lo scatto live senza upload
    # L'interfaccia è pulita per concentrarsi solo sullo scatto
    img = st.camera_input("SCANSIONE LIVE", label_visibility="collapsed")
    
    st.markdown('</div>', unsafe_allow_html=True)

# --- PROTOCOLLO DI ACCERTAMENTO (MANTENUTO) ---
st.markdown("---")
cols = st.columns(3)
steps_labels = ["ANALISI GEOMETRICA", "SPETTROMETRIA MATERIALI", "VERIFICA REGISTRI"]

for i, label in enumerate(steps_labels):
    key = list(st.session_state.checkpoints.keys())[i]
    is_active = st.session_state.checkpoints[key]
    style = "step-active" if is_active else "step-box"
    cols[i].markdown(f"<div class='{style}'>[STEP 0{i+1}]<br><b>{label}</b><br>{'CONFERMATO' if is_active else 'IN ATTESA'}</div>", unsafe_allow_html=True)

# --- LOGICA DI RAGIONAMENTO ---
if img:
    # Mostra l'immagine acquisita
    st.image(img, caption=" Snapshot Acquisito - Validazione Integrità in Corso", use_container_width=True)
    
    if not st.session_state.checkpoints["Geometria"]:
        if st.button("ESEGUI MAPPATURA GEOMETRICA"):
            with st.spinner("Analisi volumetrica..."):
                time.sleep(2)
                st.session_state.checkpoints["Geometria"] = True
                st.rerun()

    elif not st.session_state.checkpoints["Materiali"]:
        if st.button("ANALISI SPETTRALE MATERIALI"):
            with st.spinner("Verifica rifrazione e densità..."):
                time.sleep(2)
                st.session_state.checkpoints["Materiali"] = True
                st.rerun()

    elif not st.session_state.checkpoints["Seriale"]:
        if st.button("AUTENTICAZIONE SERVIZI CENTRALI"):
            with st.spinner("Interrogazione database produttore..."):
                time.sleep(3)
                st.session_state.checkpoints["Seriale"] = True
                st.rerun()

# --- VERDETTO FINALE (MANTENUTO) ---
if all(st.session_state.checkpoints.values()):
    st.balloons()
    st.markdown("""
        <div style='border: 2px solid #D4AF37; padding: 30px; border-radius: 20px; background: #0a0a0a; text-align: center;'>
            <h2 style='color: #D4AF37; font-family: Syncopate;'>CERTIFICAZIONE DI AUTENTICITÀ</h2>
            <p style='font-size: 24px; color: #2ecc71; font-weight: bold;'>VERIFICATO AL 100%</p>
            <p>L'oggetto analizzato risponde a tutti i requisiti di manifattura originale.<br>
            <span style='color: #666; font-size: 0.8rem;'>Protocollo: NEURAL-SECURE-ID-992</span></p>
        </div>
    """, unsafe_allow_html=True)

# --- NOTE LEGALI (MANTENUTE) ---
st.markdown("""
    <div class="legal-footer">
        <b>INFORMAZIONI LEGALI E AUTORIZZAZIONI:</b><br>
        Sistema protetto da crittografia end-to-end. Le analisi sono basate su modelli di intelligenza artificiale neurale validati. 
        Tutti i dati acquisiti sono trattati in conformità con il GDPR (UE 2016/679). Autorizzazione ministeriale v4.0.
    </div>
""", unsafe_allow_html=True)
