import streamlit as st
import google.generativeai as genai
import plotly.graph_objects as go
from PIL import Image, ImageEnhance
import io
import time
import json
from datetime import datetime

# =================================================================
# [INFRASTRUCTURE] - CONFIGURAZIONE GEMINI PRO 
# =================================================================
# La tua chiave è integrata per il riconoscimento universale
GEMINI_API_KEY = "AIzaSyDFVg2nb57u02SmuVq76Sy2q157a0lkJl0"
genai.configure(api_key=GEMINI_API_KEY)

class GlobalRecognitionEngine:
    """Motore di analisi universale per qualsiasi categoria di oggetto."""
    def __init__(self):
        # Utilizziamo 1.5 Flash per velocità, ma con istruzioni da 'Pro'
        self.model = genai.GenerativeModel('gemini-1.5-flash')

    def analyze_any_object(self, image_file):
        try:
            img = Image.open(image_file)
            
            # PROMPT UNIVERSALE DI CLASSIFICAZIONE
            # Questo istruisce l'IA a non fermarsi alla superficie
            prompt = """
            SISTEMA DI IDENTIFICAZIONE UNIVERSALE VERIF.AI.
            Analizza l'immagine e identifica l'oggetto indipendentemente dalla categoria.
            REGOLE:
            1. CATEGORIA: Indica la categoria merceologica esatta (es. Elettronica, Arredamento, Fashion, Meccanica).
            2. BRAND: Identifica il produttore o la marca visibile. Se non presente, indica 'Non Rilevato'.
            3. MODEL: Nome esatto del modello o codice identificativo.
            4. AUTHENTICITY: Valuta se i loghi e i materiali sembrano originali (0-100%).
            
            RISPONDI SOLO IN FORMATO JSON:
            {
                "category": "CATEGORIA",
                "brand": "MARCA",
                "model": "MODELLO",
                "confidence": 0-100,
                "technical_details": "Descrizione approfondita dell'oggetto"
            }
            """
            
            response = self.model.generate_content([prompt, img])
            # Estrazione sicura del JSON
            json_str = response.text.replace('```json', '').replace('```', '').strip()
            return json.loads(json_str)
        except Exception as e:
            return {"error": str(e), "category": "ERRORE", "brand": "RETRY", "model": "RETRY"}

# =================================================================
# [UI/UX INTERFACE] - DESIGN PROFESSIONALE
# =================================================================
def bootstrap_universal_app():
    st.set_page_config(page_title="VERIF.AI UNIVERSAL", layout="wide")

    # CSS Industrial Gold & Carbon
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Syncopate:wght@700&family=JetBrains+Mono:wght@400;700&display=swap');
        .stApp { background-color: #050505; color: #E0E0E0; font-family: 'JetBrains Mono'; }
        .main-title { font-family: 'Syncopate'; color: #D4AF37; text-align: center; letter-spacing: 15px; padding: 40px; }
        .side-panel { background: #111; border-radius: 20px; padding: 30px; border-left: 5px solid #D4AF37; box-shadow: 0 10px 30px rgba(0,0,0,0.5); }
        .label { color: #555; font-size: 0.65rem; letter-spacing: 2px; text-transform: uppercase; margin-top: 20px; }
        .value { font-family: 'Syncopate'; color: #D4AF37; font-size: 1.1rem; border-bottom: 1px solid #222; padding-bottom: 5px; }
        .status-verified { color: #00FF00; font-weight: bold; background: rgba(0,255,0,0.1); padding: 5px 15px; border-radius: 5px; }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("<h1 class='main-title'>VERIF.AI UNIVERSAL</h1>", unsafe_allow_html=True)

    engine = GlobalRecognitionEngine()

    col_scanner, col_analytics = st.columns([2, 1], gap="large")

    with col_scanner:
        st.write("📡 **INTERFACCIA DI ACQUISIZIONE OTTICA**")
        cam_img = st.camera_input("SCANNER", label_visibility="collapsed")
        if cam_img:
            st.image(cam_img, use_container_width=True)

    with col_analytics:
        st.markdown("<div class='side-panel'>", unsafe_allow_html=True)
        st.subheader("📝 DIAGNOSTICA DETTAGLIATA")
        
        if cam_img:
            with st.status("Analisi Universale in corso...", expanded=True) as s:
                data = engine.analyze_any_object(cam_img)
                time.sleep(1)
                s.update(label="✅ Identificazione Completata", state="complete")
            
            # TENDINA DI DESTRA - RISULTATI IMPECCABILI
            st.markdown("<p class='label'>Categoria Oggetto</p>", unsafe_allow_html=True)
            st.markdown(f"<p class='value'>{data.get('category')}</p>", unsafe_allow_html=True)
            
            st.markdown("<p class='label'>Marchio / Brand</p>", unsafe_allow_html=True)
            st.markdown(f"<p class='value'>{data.get('brand')}</p>", unsafe_allow_html=True)
            
            st.markdown("<p class='label'>Modello Specifico</p>", unsafe_allow_html=True)
            st.markdown(f"<p class='value'>{data.get('
