import google.generativeai as genai
from PIL import Image
import json

class VerifAiCore:
    def __init__(self, api_key):
        genai.configure(api_key=api_key)
        # Questa è la chiamata più compatibile in assoluto per gli ambienti Cloud
        self.model = genai.GenerativeModel('gemini-pro-vision')

    def analyze_object(self, image_input):
        try:
            img = Image.open(image_input)
            
            # Prompt semplificato per massimizzare la compatibilità API
            prompt = "Identify this object. Return ONLY a JSON with keys: category, brand, model, confidence."
            
            response = self.model.generate_content([prompt, img])
            
            # Estrazione del testo e pulizia totale
            res_text = response.text.strip()
            # Rimuove blocchi di codice se l'IA li inserisce
            if "{" in res_text:
                res_text = res_text[res_text.find("{"):res_text.rfind("}")+1]
            
            return json.loads(res_text)
        except Exception as e:
            # Se gemini-pro-vision fallisce, tentiamo il fallback automatico su 1.5-flash
            try:
                self.model = genai.GenerativeModel('gemini-1.5-flash')
                response = self.model.generate_content([prompt, img])
                res_text = response.text.strip()
                if "{" in res_text:
                    res_text = res_text[res_text.find("{"):res_text.rfind("}")+1]
                return json.loads(res_text)
            except:
                return {
                    "category": "Errore", 
                    "brand": "N/A", 
                    "model": "MODELLO NON SUPPORTATO - CONTROLLA API KEY", 
                    "confidence": 0
                }
