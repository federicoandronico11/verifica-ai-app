import pandas as pd
from datetime import datetime
import os

class ScanDatabase:
    """Gestore database per archiviare ogni perizia effettuata."""
    
    def __init__(self, file_path="scan_history.csv"):
        self.file_path = file_path
        if not os.path.exists(self.file_path):
            # Creazione del database iniziale
            df = pd.DataFrame(columns=["Timestamp", "ID", "Categoria", "Marca", "Modello", "Affidabilità"])
            df.to_csv(self.file_path, index=False)

    def save_scan(self, res_dict):
        """Salva il risultato di Gemini nel file CSV locale."""
        try:
            new_entry = {
                "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "ID": os.urandom(4).hex().upper(),
                "Categoria": res_dict.get("category"),
                "Marca": res_dict.get("brand"),
                "Modello": res_dict.get("model"),
                "Affidabilità": f"{res_dict.get('confidence')}%"
            }
            df = pd.read_csv(self.file_path)
            df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)
            df.to_csv(self.file_path, index=False)
            return True
        except Exception as e:
            print(f"Errore database: {e}")
            return False

    def get_history(self):
        """Recupera lo storico completo delle scansioni."""
        if os.path.exists(self.file_path):
            return pd.read_csv(self.file_path)
        return None
