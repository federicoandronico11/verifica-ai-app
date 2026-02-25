import streamlit as st
import google.generativeai as genai
from PIL import Image

# --- CONFIGURAZIONE CERVELLO REALE ---
# Inserisci qui la tua API KEY ottenuta da Google AI Studio
genai.configure(api_key="AIzaSyBgqPPSiuQw1xnPIw5cA-XZH2Akaldgl78")
model = genai.GenerativeModel('gemini-1.5-flash')

# --- DESIGN LUXURY (CONSOLIDATO) ---
st.set_page_config(page_title="VERIF.AI | GLOBAL VISION", layout="wide")
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Syncopate:wght@700&family=Share+Tech+Mono&display=swap');
    .stApp { background-color: #000; color: #D4AF37; font-family: 'Share Tech Mono', monospace; }
    .gold-logo { text-align: center; font-family: 'Syncopate'; letter-spacing: 15px; font-size: 3rem; padding: 20px; }
    .viewport { border: 2px solid #D4AF37; border-radius: 20px; overflow: hidden; margin: auto; max-width: 700px; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<div class='gold-logo'>VERIF.AI</div>", unsafe_allow_html=True)

# --- FOTOCAMERA NATIVA ---
with st.container():
    st.markdown("<div class='viewport'>", unsafe_allow_html=True)
    img_file = st.camera_input("SCAN", label_visibility="collapsed")
    st.markdown("</div>", unsafe_allow_html=True)

if img_file:
    img = Image.open(img_file)
    
    with st.status("🔮 Accesso al Database Neurale Globale...", expanded=True) as status:
        # IL MOMENTO DELLA VERITÀ: Chiediamo all'IA cosa vede realmente
        prompt = "Analizza questa immagine. Dimmi esattamente la MARCA e il MODELLO dell'oggetto inquadrato. Sii precisissimo. Se non è un oggetto, di 'Target non identificato'."
        
        try:
            response = model.generate_content([prompt, img])
            risultato = response.text
            status.update(label="✅ ANALISI COMPLETATA", state="complete")
            
            # BOX RISULTATO REALE
            st.markdown(f"""
                <div style="border: 1px solid #D4AF37; padding: 20px; border-radius: 15px; background: rgba(212,175,55,0.1); text-align: center; margin-top: 20px;">
                    <p style="color: #888; font-size: 10px;">RICONOSCIMENTO UNIVERSALE ATTIVO</p>
                    <h2 style="color: #D4AF37;">{risultato}</h2>
                </div>
            """, unsafe_allow_html=True)
            
        except Exception as e:
            st.error("Configura la tua API KEY per attivare la visione reale.")

st.markdown("<div style='text-align:center; color:#444; font-size:10px; margin-top:50px;'>PROTOCOLLO VISION V32.0 - POWERED BY GOOGLE NEURAL NETWORK</div>", unsafe_allow_html=True)
