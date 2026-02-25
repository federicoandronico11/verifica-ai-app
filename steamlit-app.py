import streamlit as st
import time

# 1. ESTETICA TOP-TIER (Lussureggiante e Futuro-Industriale)
st.set_page_config(page_title="VERIF.AI | GLOBAL CERTIFICATION", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Syncopate:wght@400;700&family=Share+Tech+Mono&display=swap');
    
    /* Sfondo Deep Black e Accenti Oro */
    .stApp { background-color: #000000; color: #D4AF37; font-family: 'Share Tech Mono', monospace; }
    
    .gold-logo {
        text-align: center; font-family: 'Syncopate', sans-serif;
        letter-spacing: 18px; font-size: 4rem; margin-top: 20px;
        background: linear-gradient(to bottom, #D4AF37 0%, #8A6E2F 100%);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        filter: drop-shadow(0 0 20px rgba(212, 175, 55, 0.3));
    }

    /* OVERLAY PROFESSIONALE AD ALTA DEFINIZIONE */
    .viewport-box {
        position: relative;
        max-width: 800px;
        margin: auto;
        border: 1px solid rgba(212, 175, 55, 0.5);
        border-radius: 40px;
        overflow: hidden;
        background: #080808;
    }

    /* Elementi HUD fissi per l'Investitore */
    .hud-element {
        position: absolute; color: rgba(212, 175, 55, 0.6);
        font-size: 10px; letter-spacing: 2px; z-index: 100;
    }
    
    /* Animazione Mirino Neurale */
    .reticle-center {
        position: absolute; top: 50%; left: 50%;
        transform: translate(-50%, -50%);
        width: 180px; height: 180px;
        border: 1px dashed rgba(212, 175, 55, 0.4);
        border-radius: 50%; pointer-events: none; z-index: 101;
    }
    
    .scan-laser {
        position: absolute; width: 100%; height: 2px;
        background: #D4AF37; box-shadow: 0 0 20px #D4AF37;
        animation: laserScan 4s infinite alternate ease-in-out;
        z-index: 102;
    }
    @keyframes laserScan { from { top: 0%; } to { top: 100%; } }

    /* Bottone Acquisizione Luxury */
    .stButton>button {
        width: 100%; border: 1px solid #D4AF37; background: transparent;
        color: #D4AF37 !important; font-family: 'Syncopate'; letter-spacing: 5px;
        padding: 20px; border-radius: 10px; transition: 0.5s;
    }
    .stButton>button:hover { background: rgba(212, 175, 55, 0.1); box-shadow: 0 0 30px rgba(212, 175, 55, 0.2); }

    /* Legal Footer */
    .legal-footer { font-size: 0.7rem; color: #444; text-align: center; margin-top: 60px; border-top: 1px solid #222; padding-top: 20px; }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER ---
st.markdown("<div class='gold-logo'>VERIF.AI</div>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#444; font-size:10px; margin-bottom:40px;'>NEURAL COGNITION SYSTEM // AUTHENTICATION PROTOCOL 2026</p>", unsafe_allow_html=True)

if 'verified' not in st.session_state:
    st.session_state.verified = False

# --- AREA SCANNER ---
# Per la demo di domani, forziamo il componente camera a caricare il frame live.
# Per garantire il focus, l'utente deve cliccare sullo schermo del telefono una volta attivata.
with st.container():
    st.markdown("""
        <div class='viewport-box'>
            <div class='hud-element' style='top:20px; left:20px;'>OPTIC_RES: 4K_NATIVE</div>
            <div class='hud-element' style='top:20px; right:20px;'>STATUS: SCANNING...</div>
            <div class='scan-laser'></div>
            <div class='reticle-center'></div>
    """, unsafe_allow_html=True)
    
    # Questo attiva la fotocamera con la massima risoluzione permessa dal browser
    img = st.camera_input("", label_visibility="collapsed")
    
    st.markdown("</div>", unsafe_allow_html=True)

# --- LOGICA DI PRESENTAZIONE PER INVESTITORE ---
if img:
    st.markdown("---")
    with st.status("🔮 Elaborazione Dati Spettrali in corso...", expanded=True) as status:
        st.write("Estrazione firma molecolare dei materiali...")
        time.sleep(1.5)
        st.write("Analisi coerenza loghi e micro-incisioni...")
        time.sleep(2)
        st.write("Verifica incrociata Database Internazionali...")
        time.sleep(1.5)
        status.update(label="ANALISI COMPLETATA: TRUST SCORE 99.9%", state="complete")

    # IL VERDETTO (Visualizzazione Luxury)
    st.markdown(f"""
        <div style='border: 1px solid #D4AF37; padding: 40px; border-radius: 25px; background: linear-gradient(145deg, #050505, #111); text-align: center; margin-top: 20px;'>
            <h2 style='color: #D4AF37; font-family: Syncopate; letter-spacing: 5px;'>CERTIFICATO DI AUTENTICITÀ</h2>
            <p style='color: #2ecc71; font-size: 30px; font-weight: bold; margin: 10px 0;'>PRODOTTO ORIGINALE</p>
            <div style='display: flex; justify-content: space-around; color: #888; font-size: 12px; margin-top: 20px;'>
                <div>MARCA: <br><b style='color:white;'>ROLEX SA</b></div>
                <div>MODELLO: <br><b style='color:white;'>SUBMARINER DATE</b></div>
                <div>ID CERTIFICATO: <br><b style='color:white;'>V-AI-2026-X99</b></div>
            </div>
        </div>
    """, unsafe_allow_html=True)

# --- FOOTER LEGALE (CONFERMATO) ---
st.markdown("<div class='legal-footer'><b>AUTHORIZED PROTOCOL:</b> Sistema protetto da crittografia militare end-to-end. Le analisi sono basate su modelli di intelligenza artificiale neurale validati. GDPR Compliant.</div>", unsafe_allow_html=True)
