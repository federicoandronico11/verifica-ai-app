import google.generativeai as genai
from PIL import Image
import json

class VerifAiCore:
    def __init__(self, api_key):
        genai.configure(api_key=api_key)
        # Passiamo al modello Pro: più stabile e con supporto totale
        self.model = genai.GenerativeModel('gemini-1.5-pro')

    def analyze_object(self, image_input):
        try:
            img = Image.open(image_input)
            
            prompt = """
            [SYSTEM: UNIVERSAL IDENTIFIER V1]
            Analizza l'immagine e identifica l'oggetto in modo impeccabile.
            Restituisci ESATTAMENTE questo formato JSON:
            {
                "category": "Categoria dell'oggetto",
                "brand": "Marca",
                "model": "Modello esatto",
                "confidence": 99,
                "verdict": "AUTHENTIC"
            }
            """
            
            # Generazione contenuto con gestione errori specifica
            response = self.model.generate_content([prompt, img])
            
            # Pulizia e validazione del JSON
            res_text = response.text.strip()
            if "```json" in res_text:
                res_text = res_text.split("```json")[1].split("```")[0].strip()
            
            return json.loads(res_text)
        except Exception as e:
            return {
                "category": "Errore", 
                "brand": "Riprova", 
                "model": f"Errore di compatibilità: {str(e)}", 
                "confidence": 0, 
                "verdict": "ERROR"
            }
