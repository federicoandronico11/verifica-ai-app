import google.generativeai as genai
from PIL import Image
import json

class VerifAiCore:
    def __init__(self, api_key):
        self.api_key = api_key
        try:
            # Configurazione esplicita per evitare il 404
            genai.configure(api_key=self.api_key)
            # Utilizziamo il nome modello standard testato su Streamlit Cloud
            self.model = genai.GenerativeModel('gemini-1.5-flash')
        except Exception:
            self.model = None

    def analyze_object(self, image_input):
        if not self.model:
            return {"category": "Errore", "brand": "CONFIG_FAIL", "model": "Riavvia App", "confidence": 0}
            
        try:
            img = Image.open(image_input)
            
            # Prompt semplificato per ridurre il carico di dati
            prompt = "Identify this object. Return JSON: {category, brand, model, confidence}"
            
            # Chiamata diretta
            response = self.model.generate_content([prompt, img])
            
            # Parsing robusto per estrarre il JSON anche se l'IA aggiunge testo extra
            res_text = response.text.strip()
            start_idx = res_text.find("{")
            end_idx = res_text.rfind("}") + 1
            if start_idx != -1 and end_idx != -1:
                res_text = res_text[start_idx:end_idx]
            
            return json.loads(res_text)
            
        except Exception as e:
            err_str = str(e)
            # Se l'errore è ancora 404, forniamo un'istruzione chiara
            if "404" in err_str:
                return {"category": "Errore 404", "brand": "API_ENDPOINT_MISMATCH", "model": "Aggiorna requirements.txt", "confidence": 0}
            return {"category": "Errore", "brand": "Dettaglio", "model": err_str[:50], "confidence": 0}
