import streamlit as st
import google.generativeai as genai
import plotly.graph_objects as go
from PIL import Image, ImageEnhance
import io
import time
import json
from datetime import datetime

# =================================================================
# [CORE CONFIGURATION] - CHIAVE GOOGLE GEMINI INSERITA
# =================================================================
GEMINI_API_KEY = "AIzaSyDFVg2nb57u02SmuVq76Sy2q157a0lkJl0"
genai.configure(api_key=GEMINI_API_KEY)

class VerifAiEngine:
    """Motore di intelligenza artificiale per il riconoscimento professionale."""
    def __init__(self):
        # Utilizziamo Gemini 1.5 Flash per la massima velocità di risposta nel pitch
        self.model = genai.GenerativeModel('gemini-1.5-flash')

    def analyze_image(self, image_file):
        try:
            img = Image.open(image_file)
            
            # Prompt ingegnerizzato per evitare il risultato "None"
            prompt = """
            Analizza questa immagine come un perito esperto. 
            Identifica il marchio e il modello dell'oggetto inquadrato.
            Se l'oggetto è uno smartphone, specifica versione e colore.
            Fornisci i dati ESATTAMENTE in questo formato JSON:
            {
                "brand": "NOME MARCHIO",
                "model": "MODELLO ESATTO",
                "confidence": 0-100,
                "verdict": "AUTHENTIC / NOT_RECOGNIZED",
                "notes": "Breve descrizione tecnica"
            }
            """
            
            response = self.model.generate_content([prompt, img])
            
            # Pulizia della risposta per estrarre il JSON puro
            raw_text = response.text.replace('```json', '').replace('```', '').strip()
            return json.loads(raw_text)
        except Exception as e:
            return {"error": str(e), "brand": "CONNECTION_ERROR", "model": "RETRY_REQUIRED"}

# =================================================================
# [UI DESIGN & WORKFLOW]
# =================================================================
def main():
    st.set_page_config(page_title="VERIF.AI | GLOBAL TERMINAL", layout="wide")
    
    # CSS Luxury Industrial
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Syncopate:wght@700&family=JetBrains+Mono:wght@400;700&display=swap');
        .stApp { background-color: #000000; color: #FFFFFF; font-family: 'JetBrains Mono'; }
        .header-container { padding: 30px; text-align: center; border-bottom: 2px solid #D4AF37; margin-bottom: 30px; }
        .title-gold { font-family: 'Syncopate'; color: #D4AF37; letter-spacing: 12px; font-size: 2.5rem; }
        .diag-panel { background: #111111; border: 1px solid #333; border-radius: 20px; padding: 25px; }
        .label-style { color: #555; font-size: 0.7rem; letter-spacing: 2px; text-transform: uppercase; margin-top: 15px; }
        .value-style { font-family: 'Syncopate'; color: #D4AF37; font-size: 1.3rem; margin-bottom: 10px; }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("<div class='header-container'><h1 class='title-gold'>VERIF.AI</h1></div>", unsafe_allow_html=True)

    engine = VerifAiEngine()

    col_cam, col_data = st.columns([2, 1], gap="large")

    with col_cam:
        st.subheader("📡 NEURAL SCANNER")
        cam_data = st.camera_input("SCANNER_INPUT", label_visibility="collapsed")
        if cam_data:
            st.image(cam_data, use_container_width=True)

    with col_data:
        st.markdown("<div class='diag-panel'>", unsafe_allow_html=True)
        st.subheader("📊 ANALYTICS")
        
        if cam_data:
            with st.status("Interrogazione Google Neural Network...", expanded=True) as status:
                result = engine.analyze_image(cam_data)
                time.sleep(1)
                status.update(label="✅ Analisi Completata", state="complete")
            
            # Visualizzazione Risultati nella tendina di destra
            st.markdown("<p class='label-style'>Identified Brand</p>", unsafe_allow_html=True)
            st.markdown(f"<p class='value-style'>{result.get('brand')}</p>", unsafe_allow_html=True)
            
            st.markdown("<p class='label-style'>Model & Revision</p>", unsafe_allow_html=True)
            st.markdown(f"<p class='value-style'>{result.get('model')}</p>", unsafe_allow_html=True)
            
            # Grafico Gauge per Autenticità
            score = result.get('confidence', 0)
            fig = go.Figure(go.Indicator(
                mode = "gauge+number",
                value = score,
                gauge = {'bar': {'color': "#D4AF37"}, 'bgcolor': "#222", 'axis': {'range': [0, 100]}},
                number = {'suffix': "%", 'font': {'color': "#D4AF37"}}
            ))
            fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', font={'color': "white"}, height=200, margin=dict(l=20, r=20, t=20, b=20))
            st.plotly_chart(fig, use_container_width=True)
            
            st.markdown(f"<p class='label-style'>Technical Verdict</p>", unsafe_allow_html=True)
            st.success(result.get('verdict'))
        else:
            st.info("In attesa di acquisizione ottica...")
        
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<br><hr style='border-color:#222;'><center><small style='color:#333;'>SYSTEM_STATUS: SECURE | ENGINE: GEMINI-1.5-FLASH | KEY_STATUS: ACTIVE</small></center>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
