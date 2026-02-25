from google import genai
from PIL import Image
import json
import time

class VerifAiCore:
    def __init__(self, api_key):
        self.api_key = api_key
        try:
            # Specifichiamo i parametri di connessione 2026
            self.client = genai.Client(
                api_key=self.api_key,
                http_options={'api_version': 'v1alpha'} # Forza l'ultima versione API
            )
            # Nome modello aggiornato per il 2026
            self.model_id = "gemini-1.5-flash-latest"
        except Exception:
            self.client = None

    def analyze_object(self, image_input):
        if not self.client:
            return {"category": "ERRORE", "brand": "INIT_FAIL", "model": "Check API Key", "confidence": 0}
            
        try:
            img = Image.open(image_input)
            
            # Chiamata con gestione esplicita dei parametri
            response = self.client.models.generate_content(
                model=self.model_id,
                contents=["Analizza questa immagine. Restituisci SOLO un oggetto JSON: {category, brand, model, confidence}", img]
            )
            
            # Parsing robusto
            res_text = response.text.strip()
            if "```json" in res_text:
                res_text = res_text.split("```json")[1].split("```")[0]
            elif "{" in res_text:
                res_text = res_text[res_text.find("{"):res_text.rfind("}")+1]
                
            return json.loads(res_text)
            
        except Exception as e:
            # Se vedi ancora 404, significa che la tua API Key non ha accesso a questo modello
            error_msg = str(e)
            return {
                "category": "ERRORE_CONNESSIONE",
                "brand": "GOOGLE_CLOUD",
                "model": "Modello non trovato o API non attiva",
                "confidence": 0
            }
