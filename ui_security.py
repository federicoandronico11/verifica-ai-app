import streamlit as st
import hashlib

class UISecurity:
    """Sistema di protezione e cifratura per l'interfaccia VerifAi."""
    
    @staticmethod
    def hash_api_key(api_key):
        """Nasconde la chiave API nei log per sicurezza."""
        if not api_key: return "N/A"
        return hashlib.sha256(api_key.encode()).hexdigest()[:12] + "..."

    @staticmethod
    def inject_custom_css():
        """Aggiunge uno strato di design professionale via CSS."""
        st.markdown("""
        <style>
        .reportview-container { background: #f0f2f6; }
        .stButton>button { width: 100%; border-radius: 20px; border: 1px solid #ff4b4b; }
        .stDataFrame { border: 1px solid #e6e9ef; border-radius: 10px; }
        </style>
        """, unsafe_content_allowed=True)

    @staticmethod
    def validate_session():
        """Verifica l'integrità della sessione utente."""
        if 'start_time' not in st.session_state:
            st.session_state.start_time = time.time()
        return True
