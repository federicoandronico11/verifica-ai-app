import google.generativeai as genai
from PIL import Image
import json
import os

class VerifAiCore:
    def __init__(self, api_key):
        self.api_key = api_key
        # Configurazione con trasporto forzato 'rest' (più stabile per Cloud)
        try:
            genai.configure(api_key=self.api_key, transport='rest')
            self.model = genai.GenerativeModel('gemini-1.5-flash')
        except Exception:
            self.model = None

    def analyze_object(self, image_input):
        if not self.api_key:
            return {"category": "ERRORE", "brand": "CHIAVE MANCANTE", "model": "Inserire API Key", "confidence": 0}
            
        try:
            img = Image.open(image_input)
            # Prompt rinforzato per forzare la risposta JSON
            prompt = """
            Return ONLY a JSON object for this item:
            {
              "category": "Object category",
              "brand": "Manufacturer",
              "model": "Exact model name",
              "confidence": 95
            }
            """
            
            response = self.model.generate_content([prompt, img])
            
            # Parsing iper-resistente
            res_text = response.text.strip()
            if "{" in res_text:
                res_text = res_text[res_text.find("{"):res_text.rfind("}")+1]
            return json.loads(res_text)
            
        except Exception as e:
            # Diagnostica specifica per l'utente
            err = str(e)
            if "403" in err or "permission" in err.lower():
                return {"category": "Errore", "brand": "PERMESSI NEGATI", "model": "Abilita 'Google AI Studio' nel tuo Google Cloud", "confidence": 0}
            return {"category": "Errore", "brand": "DEBUG", "model": err[:40], "confidence": 0}
