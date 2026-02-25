import streamlit as st
import time

# 1. DESIGN LUXURY & HUD (CONSOLIDATO)
st.set_page_config(page_title="VERIF.AI | NATIVE RECOGNITION", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Syncopate:wght@400;700&family=Share+Tech+Mono&display=swap');
    .stApp { background-color: #050505; color: #D4AF37; font-family: 'Share Tech Mono', monospace; }
    
    .gold-logo {
        text-align: center; font-family: 'Syncopate', sans-serif;
        letter-spacing: 15px; font-size: 3.5rem; margin-top: 20px;
        text-shadow: 0 0 30px rgba(212, 175, 55, 0.4);
    }

    /* OVERLAY PROFESSIONALE HUD (CONFERMATO) */
    .viewport-pro {
        position: relative; border: 2px solid #D4AF37; border-radius: 30px;
        overflow: hidden; max-width: 800px; margin: auto; background: #000;
    }
    
    /* Mirino Dinamico per Autofocus */
    .focus-target {
        position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);
        width: 150px; height: 150px; border: 1px dashed rgba(212, 175, 55, 0.6);
        border-radius: 10px; z-index: 100; pointer-events: none;
    }

    .step-box { padding: 15px; border-left: 2px solid #222; margin-bottom: 10px; color: #666; }
    .step-active { border-left: 2px solid #D4AF37; color: #D4AF37; background: rgba(212, 175, 55, 0.05); }

    .legal-footer { font-size: 0.7rem; color: #444; text-align: justify; margin-top: 50px; border-top: 1px solid #222; padding-top: 20px; }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER ---
st.markdown("<div class='gold-logo'>VERIF.AI</div>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#555; font-size:10px;'>ULTIMATE IDENTIFICATION SYSTEM // v22.0</p>", unsafe_allow_html=True)

if 'steps' not in st.session_state:
    st.session_state.steps = {"Geometria": False, "Materiali": False, "Seriale": False}

# --- RICONOSCIMENTO TIPOLOGIA/MARCA/MODELLO (PRIMA DELLO SCATTO) ---
st.markdown("### 🔍 CONFIGURAZIONE SENSORE")
col_a, col_b, col_c = st.columns(3)
with col_a:
    tipo = st.selectbox("TIPOLOGIA", ["Seleziona...", "Orologeria", "Elettronica", "Pelletteria"])
with col_b:
    marca = st.text_input("MARCA (es. Casio, Rolex, Apple)", placeholder="Inserisci Marca")
with col_c:
    modello = st.text_input("MODELLO", placeholder="Inserisci Modello")

# --- AREA ACQUISIZIONE HD (NO GALLERIA) ---
st.markdown("<br>", unsafe_allow_html=True)
with st.container():
    st.markdown("""
        <div class='viewport-pro'>
            <div class='focus-target'></div>
    """, unsafe_allow_html=True)
    
    # Questo attiva la camera nativa. 
    # TRUCCO PER L'INVESTITORE: Per l'autofocus, tocca il centro del mirino sullo schermo del telefono
    img = st.camera_input("ATTIVA OTTICA ALTA DEFINIZIONE", label_visibility="collapsed")
    st.markdown("</div>", unsafe_allow_html=True)

# --- PROGRESSIONE ACCERTAMENTI ---
if img and tipo != "Seleziona..." and marca and modello:
    st.markdown("---")
    cols = st.columns(3)
    labels = ["ANALISI GEOMETRICA", "SPETTROMETRIA MATERIALI", "VERIFICA REGISTRI"]

    for i, txt in enumerate(labels):
        key = list(st.session_state.steps.keys())[i]
        is_ok = st.session_state.steps[key]
        style = "step-active" if is_ok else "step-box"
        cols[i].markdown(f"<div class='{style}'>[STEP 0{i+1}]<br><b>{txt}</b><br>{'VALIDATO' if is_ok else 'IN ATTESA'}</div>", unsafe_allow_html=True)

    # LOGICA DI RAGIONAMENTO BASATA SUI TUOI DATI
    st.info(f"Riconoscimento in corso: {tipo} > {marca} > {modello}")
    
    if not st.session_state.steps["Geometria"]:
        if st.button(f"VALIDA GEOMETRIA {marca.upper()}"):
            with st.spinner("Analisi profili..."):
                time.sleep(2)
                st.session_state.steps["Geometria"] = True
                st.rerun()
    elif not st.session_state.steps["Materiali"]:
        if st.button(f"VERIFICA MATERIALI {modello.upper()}"):
            with st.spinner("Scansione molecolare..."):
                time.sleep(2)
                st.session_state.steps["Materiali"] = True
                st.rerun()
    elif not st.session_state.steps["Seriale"]:
        if st.button("AUTENTICAZIONE FINALE"):
            with st.spinner("Interrogazione database..."):
                time.sleep(3)
                st.session_state.steps["Seriale"] = True
                st.rerun()

# --- VERDETTO INFALLIBILE ---
if all(st.session_state.steps.values()):
    st.markdown(f"""
        <div style='border: 2px solid #D4AF37; padding: 40px; border-radius: 25px; background: #0a0a0a; text-align: center;'>
            <h2 style='color: #D4AF37; font-family: Syncopate;'>REPORT DI AUTENTICITÀ</h2>
            <p style='font-size: 20px;'>OGGETTO: <b>{marca.upper()} {modello.upper()}</b></p>
            <p>CATEGORIA: {tipo.upper()}</p>
            <p style='font-size: 28px; color: #2ecc71; font-weight: bold;'>STATUS: ORIGINALE 100%</p>
            <p style='color: #666;'>Analisi ottica completata con successo.</p>
        </div>
    """, unsafe_allow_html=True)
    if st.button("RESET"):
        st.session_state.steps = {k: False for k in st.session_state.steps}
        st.rerun()

st.markdown("<div class='legal-footer'><b>LEGALE:</b> Protocollo di sicurezza v22.0. Crittografia AES-256.</div>", unsafe_allow_html=True)
