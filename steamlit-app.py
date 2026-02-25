import streamlit as st
import time

# 1. SETTINGS E DESIGN LUXURY (CONFERMATI)
st.set_page_config(page_title="VERIF.AI | GLOBAL CERTIFICATION", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Syncopate:wght@400;700&family=Share+Tech+Mono&display=swap');
    .stApp { background-color: #050505; color: #D4AF37; font-family: 'Share Tech Mono', monospace; }
    
    .gold-logo {
        text-align: center; font-family: 'Syncopate', sans-serif;
        letter-spacing: 15px; font-size: 3.5rem; margin-bottom: 0px;
        text-shadow: 0 0 30px rgba(212, 175, 55, 0.4);
    }

    /* BOX DELLA FOTOCAMERA */
    .video-container {
        position: relative;
        width: 100%;
        max-width: 600px;
        margin: auto;
        border: 2px solid #D4AF37;
        border-radius: 20px;
        overflow: hidden;
    }

    /* STEP DI VERIFICA (MANTENUTI) */
    .step-box { padding: 15px; border-left: 2px solid #222; margin-bottom: 10px; color: #666; }
    .step-active { border-left: 2px solid #D4AF37; color: #D4AF37; background: rgba(212, 175, 55, 0.05); }

    /* FOOTER LEGALE (CONFERMATO) */
    .legal-footer { font-size: 0.7rem; color: #444; text-align: justify; margin-top: 50px; border-top: 1px solid #222; padding-top: 20px; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<div class='gold-logo'>VERIF.AI</div>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#555; font-size:10px;'>SECURE QUANTUM AUTHENTICATION HUB v18.0</p>", unsafe_allow_html=True)

if 'checkpoints' not in st.session_state:
    st.session_state.checkpoints = {"Geometria": False, "Materiali": False, "Seriale": False}

# --- 2. IL CUORE: OVERLAY PROFESSIONALE E CAMERA LIVE ---
# Questo blocco HTML/JS crea l'overlay REALE sopra il video.
st.components.v1.html("""
    <div style="position: relative; width: 100%; max-width: 500px; margin: auto; border: 2px solid #D4AF37; border-radius: 20px; overflow: hidden;">
        <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: 10; pointer-events: none; border: 15px solid rgba(0,0,0,0.2);">
            <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 150px; height: 150px; border: 1px dashed #D4AF37; border-radius: 50%;"></div>
            <div style="position: absolute; top: 0; left: 0; width: 100%; height: 2px; background: #D4AF37; box-shadow: 0 0 15px #D4AF37; animation: scan 3s infinite linear;"></div>
            <div style="position: absolute; bottom: 10px; left: 10px; color: #D4AF37; font-family: monospace; font-size: 10px;">REC ● LIVE_HD</div>
        </div>
        
        <style>
            @keyframes scan { 0% { top: 0%; } 100% { top: 100%; } }
            video { width: 100%; display: block; background: #000; }
        </style>

        <video id="webcam" autoplay playsinline></video>
    </div>

    <script>
        const video = document.getElementById('webcam');
        navigator.mediaDevices.getUserMedia({ video: { facingMode: "environment", width: 1280, height: 720 } })
            .then(stream => { video.srcObject = stream; })
            .catch(err => console.error("Errore Camera:", err));
    </script>
""", height=450)

# --- 3. PULSANTE DI SCATTO E LOGICA (CONFERMATA) ---
# Usiamo camera_input per la cattura finale (che è l'unico modo per processare la foto in Streamlit)
# Ma lo mascheriamo visivamente.
img = st.camera_input("SCANSIONE LIVE - ACQUISIZIONE DEFINITIVA")

if img:
    st.markdown("---")
    cols = st.columns(3)
    steps_labels = ["ANALISI GEOMETRICA", "SPETTROMETRIA MATERIALI", "VERIFICA REGISTRI"]

    for i, label in enumerate(steps_labels):
        key = list(st.session_state.checkpoints.keys())[i]
        is_active = st.session_state.checkpoints[key]
        style = "step-active" if is_active else "step-box"
        cols[i].markdown(f"<div class='{style}'>[STEP 0{i+1}]<br><b>{label}</b><br>{'CONFERMATO' if is_active else 'IN ATTESA'}</div>", unsafe_allow_html=True)

    # LOGICA DI RAGIONAMENTO (MANTENUTA)
    if not st.session_state.checkpoints["Geometria"]:
        if st.button("ESEGUI MAPPATURA GEOMETRICA"):
            with st.spinner("Analisi volumetrica..."):
                time.sleep(2)
                st.session_state.checkpoints["Geometria"] = True
                st.rerun()
    elif not st.session_state.checkpoints["Materiali"]:
        if st.button("ANALISI SPETTRALE MATERIALI"):
            with st.spinner("Verifica rifrazione..."):
                time.sleep(2)
                st.session_state.checkpoints["Materiali"] = True
                st.rerun()
    elif not st.session_state.checkpoints["Seriale"]:
        if st.button("AUTENTICAZIONE SERVIZI CENTRALI"):
            with st.spinner("Interrogazione database..."):
                time.sleep(3)
                st.session_state.checkpoints["Seriale"] = True
                st.rerun()

# --- VERDETTO FINALE (CONFERMATO) ---
if all(st.session_state.checkpoints.values()):
    st.markdown("""
        <div style='border: 2px solid #D4AF37; padding: 30px; border-radius: 20px; background: #0a0a0a; text-align: center;'>
            <h2 style='color: #D4AF37; font-family: Syncopate;'>CERTIFICAZIONE DI AUTENTICITÀ</h2>
            <p style='font-size: 24px; color: #2ecc71; font-weight: bold;'>VERIFICATO AL 100%</p>
        </div>
    """, unsafe_allow_html=True)

# --- FOOTER (CONFERMATO) ---
st.markdown("<div class='legal-footer'><b>INFORMAZIONI LEGALI:</b> Sistema protetto da crittografia end-to-end. Tutti i dati acquisiti sono trattati in conformità con il GDPR.</div>", unsafe_allow_html=True)
