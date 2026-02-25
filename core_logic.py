from google import genai
from PIL import Image
import json
import os

class VerifAiCore:
    def __init__(self, api_key):
        self.api_key = api_key
        # Nuovo inizializzatore Client SDK 2026
        try:
            self.client = genai.Client(api_key=self.api_key)
            self.model_id = "gemini-1.5-flash"
        except Exception:
            self.client = None

    def analyze_object(self, image_input):
        if not self.client:
            return {"category": "ERRORE", "brand": "CLIENT_INIT_FAILED", "model": "Check API Key", "confidence": 0}
            
        try:
            img = Image.open(image_input)
            
            # Nuova sintassi 2026 per la generazione di contenuti
            response = self.client.models.generate_content(
                model=self.model_id,
                contents=["Identify this object. Return ONLY JSON: {category, brand, model, confidence}", img]
            )
            
            # Pulizia e parsing del JSON
            raw_text = response.text.strip()
            # Rimuove eventuali tag markdown ```json ... ```
            clean_json = raw_text.replace("```json", "").replace("```", "").strip()
            
            return json.loads(clean_json)
            
        except Exception as e:
            err_str = str(e)
            if "404" in err_str or "not found" in err_str.lower():
                return {"category": "ERRORE", "brand": "ENDPOINT_DISCONNECT", "model": "Check SDK Version", "confidence": 0}
            return {"category": "ERRORE", "brand": "DEBUG", "model": err_str[:50], "confidence": 0}
