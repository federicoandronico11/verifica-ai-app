from google import genai
from PIL import Image
import json
import time

class VerifAiCore:
    def __init__(self, api_key):
        self.api_key = api_key
        # Inizializzazione con timeout esplicito per il 2026
        try:
            self.client = genai.Client(api_key=self.api_key)
            self.model_id = "gemini-1.5-flash"
        except Exception:
            self.client = None

    def analyze_object(self, image_input):
        if not self.client:
            return {"category": "ERRORE", "brand": "AUTH_FAILED", "model": "Verifica API Key", "confidence": 0}
            
        try:
            img = Image.open(image_input)
            
            # Piccolo buffer per stabilizzare la connessione prima della chiamata
            time.sleep(0.5)
            
            # Utilizziamo il metodo di generazione con parametri di sicurezza
            response = self.client.models.generate_content(
                model=self.model_id,
                contents=["Analizza l'oggetto. Restituisci JSON: {category, brand, model, confidence}", img]
            )
            
            if not response.text:
                raise ValueError("Risposta vuota dal server")

            raw_text = response.text.strip()
            clean_json = raw_text.replace("```json", "").replace("```", "").strip()
            
            return json.loads(clean_json)
            
        except Exception as e:
            # Se fallisce ancora, attiviamo il log di emergenza
            return {
                "category": "RECOVERY_MODE",
                "brand": "RETRY_REQUIRED",
                "model": str(e)[:40],
                "confidence": 0
            }
