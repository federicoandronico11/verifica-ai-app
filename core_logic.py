from google import genai
from PIL import Image
import json
import time

class VerifAiCore:
    def __init__(self, api_key):
        self.api_key = api_key
        try:
            # Forziamo il client sulla versione v1beta (la più permissiva)
            self.client = genai.Client(api_key=self.api_key, http_options={'api_version': 'v1beta'})
            self.models = ["gemini-1.5-flash", "gemini-2.0-flash-exp", "gemini-pro-vision"]
        except Exception:
            self.client = None

    def analyze_object(self, image_input):
        if not self.client or not self.api_key.startswith("AIza"):
            return {"category": "ERRORE", "brand": "KEY_INVALIDA", "model": "Usa una chiave AIza...", "confidence": 0}
            
        img = Image.open(image_input)
        
        for model_id in self.models:
            try:
                response = self.client.models.generate_content(
                    model=model_id,
                    contents=["Analizza l'oggetto. Restituisci JSON: {category, brand, model, confidence}", img]
                )
                if response.text:
                    clean_txt = response.text.strip().replace("```json", "").replace("```", "")
                    return json.loads(clean_txt[clean_txt.find("{"):clean_txt.rfind("}")+1])
            except Exception:
                continue
        
        return {"category": "ERRORE_SISTEMA", "brand": "GOOGLE_AUTH", "model": "Verifica Key su AI Studio", "confidence": 0}
        
