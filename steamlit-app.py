import streamlit as st
import requests
from PIL import Image
import io
import time

# --- CONFIGURAZIONE CORE ---
HF_TOKEN = "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" 
API_URL = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-large"
headers = {"Authorization": f"Bearer {HF_TOKEN}"}

# --- SETUP PAGINA ---
st.set_page_config(page_title="VERIF.AI | SUPREME AUTH", layout="wide", initial_sidebar_state="collapsed")

# --- CSS PREMIUM ---

    <style>
    @import url('https://fonts.googleapis.com/css2?family=Syncopate:wght@400;700&family=Share+Tech+Mono&display=swap');
    .stApp { background-color: #050505; color: #D4AF37; font-family: 'Share Tech Mono', monospace; }
    .header-container { text-align: center; padding: 40px 0; border-bottom: 1px solid rgba(212,175,55,0.1); }
    .gold-logo { font-family: 'Syncopate', sans-serif; letter-spacing: 20px; font-size: 3.2rem; text-shadow: 0 0 30px rgba(212,175,55,0.4); }
    .viewport-container {
        position: relative; border: 2px solid #D4AF37; border-radius: 40px;
        padding: 10px; background: #000; box-shadow: 0 0 50px rgba(212,175,55,0.1);
        max-width: 800px; margin: auto; overflow: hidden;
    }
    .scan-line {
        position: absolute; width: 100%; height: 3px; background: #D4AF37;
        box-shadow: 0 0 20px #D4AF37; animation: moveLine 4s infinite linear; z-index: 100;
    }
    @keyframes moveLine { 0% { top: 0%; } 100% { top: 100%; } }
    .id-card {
        background: linear-gradient(135deg, #0f0f0f 0%, #1a1a1a 100%);
        border: 1px solid #D4AF37; border-radius: 20px; padding: 25px;
        margin-top: 20px; text-align: left; box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    }
    .res-label { font-size: 0.6rem; color: #666; letter-spacing: 2px; text-transform: uppercase; margin-bottom: 5px; }
    .res-value { font-family: 'Syncopate'; font-size: 1.1rem; color: #D4AF37; margin-bottom: 15px; }
    .status-authentic { color: #2ecc71; font-weight: bold; border: 1px solid #2ecc71; padding: 4px 12px; border-radius:
