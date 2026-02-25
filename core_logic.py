import google.generativeai as genai
from PIL import Image
import json

class VerifAiCore:
    def __init__(self, api_key):
        self.api_key = api_key
        try:
            genai.configure(api_key=self.api_key)
            # Proviamo il modello più universale in assoluto
            self.model = genai.GenerativeModel('gemini-1.5-flash')
        except Exception as e:
            self.model = None

    def analyze_object(self, image_input):
        if not self.api_key or self.api_key == "INSERISCI_QUI":
            return {"category": "Errore", "brand": "API KEY MANCANTE", "model": "Inserisci la chiave", "confidence": 0}
        
        try:
            img = Image.open(image_input)
            prompt = "Identify: Category, Brand, Model. Return JSON only."
            
            response = self.model.generate_content([prompt, img])
            
            # Estrazione sicura del testo
            res_text = response.text.strip()
            if "{" in res_text:
                res_text = res_text[res_text.find("{"):res_text.rfind("}")+1]
            return json.loads(res_text)
            
        except Exception as e:
            error_msg = str(e)
            if "API_KEY_INVALID" in error_msg:
                return {"category": "Errore", "brand": "API KEY NON VALIDA", "model": "Rigenera la chiave su AI Studio", "confidence": 0}
            elif "429" in error_msg:
                return {"category": "Errore", "brand": "LIMITE RAGGIUNTO", "model": "Troppe richieste, attendi 60s", "confidence": 0}
            else:
                return {"category": "Errore", "brand": "DETTAGLIO:", "model": error_msg[:50], "confidence": 0}
