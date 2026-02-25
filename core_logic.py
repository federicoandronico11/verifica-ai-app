from google import genai
from PIL import Image
import json
import time

class VerifAiCore:
    def __init__(self, api_key="AIzaSyAgVN8OcgZYRzzD6nrpRONNONLWogfKmFw"):
        self.api_key = api_key
        try:
            # Configurazione Client 2026
            self.client = genai.Client(api_key=self.api_key)
            self.model_id = "gemini-1.5-flash"
        except Exception:
            self.client = None

    def analyze_object(self, image_input):
        if not self.client:
            return {"category": "ERRORE", "brand": "AUTH", "model": "Configurazione fallita", "confidence": 0}
            
        try:
            img = Image.open(image_input)
            
            # Chiamata diretta al modello
            response = self.client.models.generate_content(
                model=self.model_id,
                contents=["Analizza l'oggetto. Restituisci SOLO JSON: {category, brand, model, confidence}", img]
            )
            
            if response.text:
                txt = response.text
                start = txt.find('{')
                end = txt.rfind('}') + 1
                return json.loads(txt[start:end])
                
        except Exception as e:
            return {
                "category": "ERRORE_TECNICO",
                "brand": "GOOGLE_API",
                "model": str(e)[:50],
                "confidence": 0
            }
