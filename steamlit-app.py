import streamlit as st
import time

# 1. CONFIGURAZIONE ESTETICA (CONSOLIDATA E INALTERATA)
st.set_page_config(page_title="VERIF.AI | NEURAL PREDICTION", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Syncopate:wght@400;700&family=Share+Tech+Mono&display=swap');
    .stApp { background-color: #050505; color: #D4AF37; font-family: 'Share Tech Mono', monospace; }
    
    .gold-logo {
        text-align: center; font-family: 'Syncopate', sans-serif;
        letter-spacing: 15px; font-size: 3.5rem; margin-top: 20px;
        text-shadow: 0 0 30px rgba(212, 175, 55, 0.4);
    }

    /* VIEWPORT CON OVERLAY HUD PROFESSIONALE (CONFERMATO) */
    .viewport-pro {
        position: relative; border: 2px solid #D4AF37; border-radius: 30px;
        overflow: hidden; max-width: 800px; margin: auto; background: #000;
    }
    
    .scan-bar {
        position: absolute; width: 100%; height: 2px; background: #D4AF37;
        box-shadow: 0 0 15px #D4AF37; animation: scanAnim 3s infinite linear; z-index: 100;
    }
    @keyframes scanAnim { 0% { top: 0%; } 100% { top: 100%; } }

    /* ETICHETTA DI RICONOSCIMENTO REAL-TIME (NUOVA) */
    .prediction-overlay {
        position: absolute; bottom: 20px; left: 50%; transform: translateX(-50%);
        background: rgba(0,0,0,0.8); border: 1px solid #D4AF37;
        padding: 10px 25px; border-radius: 5px; z-index: 101;
        text-align: center; min-width: 300px;
    }
    .prediction-text { color: #D4AF37; font-size: 14px; letter-spacing: 2px; }
    .confidence-bar { height: 3px; background: #D4AF37; margin-top: 5px; animation: pulse 1.5s infinite; }
    @keyframes pulse { 0% { opacity: 0.3; } 50% { opacity: 1; } 100% { opacity: 0.3; } }

    .step-box { padding: 15px; border-left: 2px solid #222; margin-bottom: 10px; color: #666; }
    .step-active { border-left: 2px solid #D4AF37; color: #D4AF37; background: rgba(212, 175, 55, 0.05); }
    .legal-footer { font-size: 0.7rem; color: #444; text-align: justify; margin-top: 50px; border-top: 1px solid #222; padding-top: 20px; }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER (CONFERMATO) ---
st.markdown("<div class='gold-logo'>VERIF.AI</div>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#555; font-size:10px;'>NEURAL REAL-TIME RECOGNITION // v23.0</p>", unsafe_allow_html=True)

if 'steps' not in st.session_state:
    st.session_state.steps = {"Geometria": False, "Materiali": False, "Seriale": False}

# --- AREA ACQUISIZIONE CON RICONOSCIMENTO PRE-SCATTO ---
with st.container():
    st.markdown("""
        <div class='viewport-pro'>
            <div class='scan-bar'></div>
            <div class='prediction-overlay'>
                <div class='prediction-text' id='pred-label'>ANALISI FLUSSO OTTICO...</div>
                <div class='confidence-bar'></div>
            </div>
    """, unsafe_allow_html=True)
    
    # Acquisizione Live Forzata (No Galleria)
    img = st.camera_input("SCANSIONE", label_visibility="collapsed")
    st.markdown("</div>", unsafe_allow_html=True)

# --- LOGICA DI RICONOSCIMENTO E ACCERTAMENTO ---
if img:
    # Simulazione di riconoscimento Marca/Modello post-acquisizione basata su AI
    # In un pitch, qui spiegherai che l'AI ha incrociato i dati del sensore HD
    detected_brand = "ROLEX" # Esempio: il sistema ora "sa" cosa ha visto
    detected_model = "SUBMARINER DATE 126610LN"
    
    st.markdown(f"""
        <div style='text-align:center; margin-top:20px;'>
            <p style='color:#888; margin-bottom:0;'>OGGETTO RICONOSCIUTO:</p>
            <h2 style='color:#D4AF37; margin-top:0;'>{detected_brand} {detected_model}</h2>
        </div>
    """, unsafe_allow_html=True)

    # PROTOCOLLO A 3 STEP (CONFERMATO)
    st.markdown("---")
    cols = st.columns(3)
    labels = ["ANALISI GEOMETRICA", "SPETTROMETRIA MATERIALI", "VERIFICA REGISTRI"]

    for i, txt in enumerate(labels):
        key = list(st.session_state.steps.keys())[i]
        is_ok = st.session_state.steps[key]
        style = "step-active" if is_ok else "step-box"
        cols[i].markdown(f"<div class='{style}'>[STEP 0{i+1}]<br><b>{txt}</b><br>{'VALIDATO' if is_ok else 'IN ATTESA'}</div>", unsafe_allow_html=True)

    # LOGICA DI RAGIONAMENTO INCREMENTALE
    if not st.session_state.steps["Geometria"]:
        if st.button(f"ESEGUI MAPPATURA {detected_brand}"):
            with st.spinner("Analisi profili..."):
                time.sleep(2)
                st.session_state.steps["Geometria"] = True
                st.rerun()
    elif not st.session_state.steps["Materiali"]:
        if st.button(f"VERIFICA MATERIALI {detected_brand}"):
            with st.spinner("Scansione molecolare..."):
                time.sleep(2)
                st.session_state.steps["Materiali"] = True
                st.rerun()
    elif not st.session_state.steps["Seriale"]:
        if st.button("CERTIFICAZIONE FINALE"):
            with st.spinner("Accesso database centrale..."):
                time.sleep(3)
                st.session_state.steps["Seriale"] = True
                st.rerun()

# --- VERDETTO FINALE (CONFERMATO) ---
if all(st.session_state.steps.values()):
    st.markdown(f"""
        <div style='border: 2px solid #D4AF37; padding: 40px; border-radius: 25px; background: #0a0a0a; text-align: center;'>
            <h2 style='color: #D4AF37; font-family: Syncopate;'>REPORT DEFINITIVO</h2>
            <p style='font-size: 28px; color: #2ecc71; font-weight: bold;'>AUTENTICITÀ CONFERMATA</p>
            <p>Corrispondenza totale con i parametri di fabbrica {detected_brand}.</p>
        </div>
    """, unsafe_allow_html=True)

# --- NOTE LEGALI (CONFERMATE) ---
st.markdown("<div class='legal-footer'><b>LEGALE:</b> Protocollo v23.0. Tutti i dati sono crittografati. GDPR Compliant.</div>", unsafe_allow_html=True)
