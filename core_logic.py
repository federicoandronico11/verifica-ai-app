import google.generativeai as genai
from PIL import Image
import json

class VerifAiCore:
    def __init__(self, api_key):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-1.5-flash')

    def analyze_object(self, image_input):
        img = Image.open(image_input)
        
        prompt = """
        Agisci come un esperto di identificazione universale.
        Analizza l'immagine e restituisci ESATTAMENTE questo formato JSON:
        {
            "category": "Macro categoria dell'oggetto",
            "brand": "Marca rilevata",
            "model": "Modello esatto",
            "confidence": 0-100,
            "verdict": "AUTHENTIC | UNKNOWN"
        }
        """
        try:
            response = self.model.generate_content([prompt, img])
            # Pulizia per estrarre solo il JSON
            clean_res = response.text.strip().replace('```json', '').replace('```', '')
            return json.loads(clean_res)
        except Exception as e:
            return {
                "category": "Errore", 
                "brand": "N/A", 
                "model": str(e), 
                "confidence": 0, 
                "verdict": "ERROR"
            }
