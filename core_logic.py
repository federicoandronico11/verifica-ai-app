from google import genai
from PIL import Image
import json

class VerifAiCore:
    def __init__(self, api_key):
        self.api_key = api_key
        # Inizializzazione Client Universale 2026
        try:
            self.client = genai.Client(api_key=self.api_key)
            # Cambiato da 1.5 a 2.0 per evitare il 404 (modello deprecato)
            self.model_id = "gemini-2.0-flash" 
        except Exception:
            self.client = None

    def analyze_object(self, image_input):
        if not self.client:
            return {"category": "ERRORE", "brand": "API_KEY_MISSING", "model": "Inserisci Key", "confidence": 0}
            
        try:
            img = Image.open(image_input)
            
            # La nuova chiamata 'generate' automatizzata per il 2026
            response = self.client.models.generate_content(
                model=self.model_id,
                contents=["Analizza l'immagine e restituisci SOLO JSON: {category, brand, model, confidence}", img]
            )
            
            # Estrazione sicura del testo JSON
            txt = response.text
            start = txt.find('{')
            end = txt.rfind('}') + 1
            return json.loads(txt[start:end])
            
        except Exception as e:
            # Se fallisce ancora, è un problema di attivazione della Key su Google AI Studio
            return {
                "category": "ERRORE_FINALE",
                "brand": "VERIFICA_AI_STUDIO",
                "model": "Modello 2.0 non abilitato sulla tua Key",
                "confidence": 0
            }
