import pandas as pd
from datetime import datetime
import os

class ProfessionalLogger:
    """Sistema di archiviazione dati di livello enterprise per VerifAi."""
    
    def __init__(self, filename="audit_log.csv"):
        self.filename = filename
        if not os.path.exists(self.filename):
            self.create_header()

    def create_header(self):
        df = pd.DataFrame(columns=["Timestamp", "Categoria", "Marca", "Modello", "Affidabilita"])
        df.to_csv(self.filename, index=False)

    def log_scan(self, result):
        """Registra ogni scansione riuscita nel database locale."""
        new_entry = {
            "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "Categoria": result.get("category", "N/A"),
            "Marca": result.get("brand", "N/A"),
            "Modello": result.get("model", "N/A"),
            "Affidabilita": f"{result.get('confidence', 0)}%"
        }
        df = pd.read_csv(self.filename)
        df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)
        df.to_csv(self.filename, index=False)

    def get_stats(self):
        """Genera statistiche per il modulo Plotly."""
        df = pd.read_csv(self.filename)
        return df
