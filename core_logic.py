import google.generativeai as genai
from PIL import Image
import json

class VerifAiCore:
    def __init__(self, api_key):
        genai.configure(api_key=api_key)
        # Forziamo il modello specifico che Streamlit Cloud accetta sicuramente
        self.model = genai.GenerativeModel(model_name='models/gemini-1.5-flash')

    def analyze_object(self, image_input):
        try:
            img = Image.open(image_input)
            
            prompt = """
            Sei un esperto di identificazione prodotti. 
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
            
            # Utilizziamo il metodo di generazione standard
            response = self.model.generate_content([prompt, img])
            
            # Pulizia della risposta
            text_response = response.text.strip()
            if "```json" in text_response:
                text_response = text_response.split("```json")[1].split("```")[0]
            
            return json.loads(text_response)
        except Exception as e:
            return {
                "category": "Errore di Sistema", 
                "brand": "N/A", 
                "model": f"Dettaglio Errore: {str(e)}", 
                "confidence": 0, 
                "verdict": "RETRY"
            }
