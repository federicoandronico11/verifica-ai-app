from google import genai
from PIL import Image
import json

class VerifAiCore:
    def __init__(self, api_key):
        self.api_key = api_key
        try:
            self.client = genai.Client(api_key=self.api_key)
            # Lista modelli in ordine di potenza 2026
            self.models = ["gemini-2.0-flash", "gemini-1.5-flash", "gemini-1.5-flash-latest"]
        except Exception:
            self.client = None

    def analyze_object(self, image_input):
        if not self.client:
            return {"category": "ERRORE", "brand": "CONFIG", "model": "Chiave Mancante", "confidence": 0}
            
        img = Image.open(image_input)
        
        # Prova ogni modello finché uno non risponde (Niente più 404)
        for model_id in self.models:
            try:
                response = self.client.models.generate_content(
                    model=model_id,
                    contents=["Identify object. Return ONLY JSON: {category, brand, model, confidence}", img]
                )
                if response.text:
                    txt = response.text
                    start, end = txt.find('{'), txt.rfind('}') + 1
                    return json.loads(txt[start:end])
            except Exception:
                continue # Prova il modello successivo nella lista
        
        return {
            "category": "ERRORE_CRITICO",
            "brand": "GOOGLE_BLOCK",
            "model": "Controlla Fatturazione/Limiti su AI Studio",
            "confidence": 0
        }
