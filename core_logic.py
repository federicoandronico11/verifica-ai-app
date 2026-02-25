import google.generativeai as genai
from PIL import Image
import json

class VerifAiCore:
    def __init__(self, api_key):
        genai.configure(api_key=api_key)
        # Usiamo la versione stabile più recente per evitare errori 404
        self.model = genai.GenerativeModel('gemini-1.5-flash-latest')

    def analyze_object(self, image_input):
        try:
            img = Image.open(image_input)
            
            prompt = """
            Sei un esperto mondiale di catalogazione prodotti. 
            Analizza l'immagine e identifica: Categoria, Marca e Modello.
            Restituisci ESATTAMENTE questo formato JSON:
            {
                "category": "Macro categoria dell'oggetto",
                "brand": "Marca rilevata",
                "model": "Modello esatto",
                "confidence": 0-100,
                "verdict": "AUTHENTIC"
            }
            """
            
            response = self.model.generate_content([prompt, img])
            # Pulizia sicura per estrarre il JSON
            text_response = response.text.strip()
            if "```json" in text_response:
                text_response = text_response.split("```json")[1].split("```")[0]
            
            return json.loads(text_response)
        except Exception as e:
            # Ritorna l'errore nel campo modello per vederlo nell'app
            return {
                "category": "Errore Tecnico", 
                "brand": "N/A", 
                "model": f"Errore API: {str(e)}", 
                "confidence": 0, 
                "verdict": "ERROR"
            }
