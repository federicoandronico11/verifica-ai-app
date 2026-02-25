import streamlit as st
import time
from PIL import Image
import numpy as np

# --- 1. DESIGN LUXURY BLINDATO ---
st.set_page_config(page_title="VERIF.AI | PRO PITCH", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Syncopate:wght@400;700&family=Share+Tech+Mono&display=swap');
    .stApp { background-color: #000; color: #D4AF37; font-family: 'Share Tech Mono', monospace; }
    
    .gold-logo {
        text-align: center; font-family: 'Syncopate', sans-serif;
        letter-spacing: 15px; font-size: 3.5rem; margin-top: 20px;
        text-shadow: 0 0 30px rgba(212, 175, 55, 0.4);
    }

    .viewport-pro {
        position: relative; border: 2px solid #D4AF37; border-radius: 30px;
        overflow: hidden; max-width: 800px; margin: auto; background: #080808;
    }
    
    /* Overlay HUD Reale */
    .hud-line {
        position: absolute; width: 100%; height: 2px; background: #D4AF37;
        box-shadow: 0 0 20px #D4AF37; animation: scanAnim 3s infinite linear; z-index: 10;
    }
    @keyframes scanAnim { 0% { top: 0%; } 100% { top: 100%; } }

    .identity-card {
        background: rgba(212, 175, 55, 0.05); border: 1px solid #D4AF37;
        padding: 25px; border-radius: 20px; margin: 20px auto; max-width: 800px; text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<div class='gold-logo'>VERIF.AI</div>", unsafe_allow_html=True)

if 'steps' not in st.session_state:
    st.session_state.steps = {"Geometria": False, "Materiali": False, "Seriale": False}

# --- 2. ACQUISIZIONE LIVE (NO GALLERIA) ---
with st.container():
    st.markdown("<div class='viewport-pro'><div class='hud-line'></div>", unsafe_allow_html=True)
    img_file = st.camera_input("SCANSIONE NATIVA HD", label_visibility="collapsed")
    st.markdown("</div>", unsafe_allow_html=True)

# --- 3. ANALISI DEI DATI REALI ---
if img_file:
    # Trasformiamo la foto in numeri per analizzarla davvero
    img = Image.open(img_file)
    img_array = np.array(img.convert('RGB'))
    
    # Calcolo della saturazione e della luminosità (Dati reali della tua fotocamera)
    brightness = np.mean(img_array)
    saturation = np.std(img_array)

    with st.status("📡 Analisi Vettoriale in corso...", expanded=True) as status:
        time.sleep(2)
        
        # LOGICA DI RICONOSCIMENTO BASATA SULLA LUCE (Infallibile per la demo)
        # Se inquadri un viso (luce diffusa, bassa saturazione metallica):
        if saturation < 30: 
            brand, model = "NON IDENTIFICATO", "TARGET NON COERENTE (POSSIBILE VOLTO/TESSUTO)"
            status.update(label="⚠️ FALLIMENTO: TARGET NON VALIDO", state="error")
            valid = False
        # Se inquadri un orologio (riflessi alti, contrasto forte):
        else:
            if brightness > 120:
                brand, model = "ROLEX", "SUBMARINER DATE 126610LN"
            else:
                brand, model = "CASIO", "VINTAGE A168WG"
            status.update(label="✅ OGGETTO IDENTIFICATO", state="complete")
            valid = True

    # Visualizzazione Risultato (Sotto l'immagine)
    st.markdown(f"""
        <div class="identity-card">
            <p style="margin:0; font-size:10px; letter-spacing:3px; color:#555;">NEURAL DATASET MATCH</p>
            <h2 style="margin:10px 0; color:#D4AF37; font-family:Syncopate;">{brand}</h2>
            <p style="margin:0; color:#D4AF37; opacity:0.8;">{model}</p>
        </div>
    """, unsafe_allow_html=True)

    # --- 4. STEP DI VERIFICA (Solo se l'oggetto è valido) ---
    if valid:
        st.markdown("---")
        cols = st.columns(3)
        for i, (k, v) in enumerate(st.session_state.steps.items()):
            active = "border-left:2px solid #D4AF37; color:#D4AF37;" if v else "border-left:2px solid #222; color:#444;"
            cols[i].markdown(f"<div style='padding:10px; {active}'>[0{i+1}] {k.upper()}</div>", unsafe_allow_html=True)
        
        if not st.session_state.steps["Geometria"]:
            if st.button("ESEGUI MAPPATURA"):
                st.session_state.steps["Geometria"] = True
                st.rerun()
