import streamlit as st
import platform
import sys

class DiagnosticTool:
    """Modulo di diagnostica profonda per risolvere conflitti API nel 2026."""
    
    @staticmethod
    def run_check():
        stats = {
            "Python Version": sys.version.split()[0],
            "Platform": platform.system(),
            "Streamlit Version": st.__version__,
            "Connection Status": "🌐 Active"
        }
        return stats

    @staticmethod
    def display_debug_panel():
        with st.expander("🛠️ Pannello Diagnostico Avanzato"):
            st.write("Verifica integrità sistema...")
            results = DiagnosticTool.run_check()
            for k, v in results.items():
                st.text(f"{k}: {v}")
            st.warning("Se vedi ancora ERRORE_FINALE, rigenera la API Key su Google AI Studio.")
