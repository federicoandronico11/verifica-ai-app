import google.generativeai as genai
from PIL import Image
import json
import logging

class VerifAiCore:
    def __init__(self, api_key):
        self.api_key = api_key
        # Lista di modelli in ordine di stabilità per evitare il 404
        self.model_names = ['gemini-1.5-flash', 'gemini-pro-vision', 'models/gemini-1.5-flash']
        genai.configure(api_key=self.api_key)

    def analyze_object(self, image_input):
        img = Image.open(image_input)
        prompt = "Identify this object. Return JSON: {category, brand, model, confidence}"
        
        # TENTATIVO A CASCATA: Se il primo modello dà 404, passa al secondo
        for m_name in self.model_names:
            try:
                model = genai.GenerativeModel(m_name)
                response = model.generate_content([prompt, img])
                
                # Pulizia stringa JSON
                res_text = response.text.strip()
                if "{" in res_text:
                    res_text = res_text[res_text.find("{"):res_text.rfind("}")+1]
                return json.loads(res_text)
            except Exception as e:
                logging.warning(f"Modello {m_name} fallito: {e}")
                continue # Prova il prossimo modello nella lista
        
        # Se tutti falliscono
        return {
            "category": "Errore Connessione",
            "brand": "API KEY LIMIT",
            "model": "Verifica permessi su Google AI Studio",
            "confidence": 0
        }
