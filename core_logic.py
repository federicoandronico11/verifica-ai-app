from google import genai
from PIL import Image
import json
import os

class VerifAiCore:
    def __init__(self, api_key):
        # Inizializzazione Client 2026
        self.api_key = api_key
        try:
            self.client = genai.Client(api_key=self.api_key)
            self.model_id = "gemini-1.5-flash"
        except Exception as e:
            self.client = None

    def analyze_object(self, image_input):
        if not self.client:
            return {"category": "ERRORE", "brand": "CLIENT_NOT_INIT", "model": "Verifica API Key", "confidence": 0}
            
        try:
            img = Image.open(image_input)
            
            # Nuova sintassi 2026: chiamata diretta tramite client.models
            response = self.client.models.generate_content(
                model=self.model_id,
                contents=["Analizza questa immagine. Restituisci JSON: {category, brand, model, confidence}", img]
            )
            
            # Estrazione sicura del testo
            raw_text = response.text.strip()
            # Pulizia blocchi di codice Markdown se presenti
            clean_json = raw_text.replace("```json", "").replace("```", "").strip()
            
            return json.loads(clean_json)
            
        except Exception as e:
            err_msg = str(e)
            if "404" in err_msg:
                return {"category": "ERRORE", "brand": "SISTEMA_OBSOLETO", "model": "Passa a google-genai", "confidence": 0}
            return {"category": "ERRORE", "brand": "DETTAGLIO", "model": err_msg[:50], "confidence": 0}
