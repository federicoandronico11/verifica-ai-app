from google import genai
from PIL import Image
import json

class VerifAiCore:
    def __init__(self, api_key):
        # Nuovo client 2026 per Gemini
        self.client = genai.Client(api_key=api_key)
        self.model_id = "gemini-1.5-flash"

    def analyze_object(self, image_input):
        try:
            img = Image.open(image_input)
            
            # Nuova sintassi di chiamata SDK
            response = self.client.models.generate_content(
                model=self.model_id,
                contents=["Identify this object. Return ONLY JSON: {category, brand, model, confidence}", img]
            )
            
            # Estrazione testo sicura
            res_text = response.text.strip()
            if "{" in res_text:
                res_text = res_text[res_text.find("{"):res_text.rfind("}")+1]
            
            return json.loads(res_text)
            
        except Exception as e:
            err = str(e)
            if "404" in err:
                return {"category": "ERRORE", "brand": "VECCHIO_ENDPOINT", "model": "Usa google-genai", "confidence": 0}
            return {"category": "ERRORE", "brand": "DEBUG", "model": err[:50], "confidence": 0}
