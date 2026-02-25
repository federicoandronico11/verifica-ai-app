import google.generativeai as genai
from PIL import Image, ImageEnhance
import json
import logging
import uuid
from datetime import datetime

# Configurazione del Logging Industriale
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class VerifAiCore:
    """
    MOTORE LOGICO CENTRALE v90.0
    Gestisce l'intelligenza artificiale, la validazione dei dati e la sicurezza.
    """
    
    def __init__(self, api_key):
        self.api_key = api_key
        try:
            genai.configure(api_key=self.api_key)
            self.model = genai.GenerativeModel('gemini-1.5-flash')
            logger.info("Motore IA configurato correttamente.")
        except Exception as e:
            logger.error(f"Errore inizializzazione IA: {e}")
            raise

    def preprocess_image(self, image_input):
        """Ottimizza l'immagine per il riconoscimento micrometrico."""
        try:
            img = Image.open(image_input)
            # Aumentiamo la nitidezza per leggere meglio loghi e piccoli testi
            enhancer = ImageEnhance.Sharpness(img)
            img = enhancer.enhance(2.5)
            return img
        except Exception as e:
            logger.error(f"Errore pre-processing: {e}")
            return None

    def get_universal_recognition(self, pil_image):
        """Esegue il riconoscimento impeccabile di qualsiasi oggetto."""
        
        # Prompt ingegnerizzato per output JSON garantito e preciso
        prompt = """
        [AUTH_PROTOCOL_V90]
        Analizza l'immagine fornita. Identifica l'oggetto con precisione forense.
        DEVI identificare:
        1. CATEGORY: La macro-categoria merceologica.
        2. BRAND: Il marchio o produttore.
        3. MODEL: Il modello esatto o la serie.
        4. SPECS: Dettagli tecnici (materiali, colori, finiture).
        5. AUTHENTICITY_SCORE: Probabilità che sia originale (0-100).

        RISPONDI ESATTAMENTE E SOLO IN QUESTO FORMATO JSON:
        {
            "category": "...",
            "brand": "...",
            "model": "...",
            "specs": "...",
            "confidence": 0,
            "verdict": "AUTHENTIC | COUNTERFEIT | UNKNOWN"
        }
        """

        try:
            response = self.model.generate_content([prompt, pil_image])
            # Pulizia della stringa per evitare errori di parsing
            clean_res = response.text.strip().replace('```json', '').replace('```', '')
            data = json.loads(clean_res)
            
            # Aggiunta metadati di sistema
            data['scan_id'] = str(uuid.uuid4())[:13].upper()
            data['timestamp'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            return data
        except Exception as e:
            logger.error(f"Errore durante l'analisi neurale: {e}")
            return {
                "category": "ERROR", 
                "brand": "RETRY_REQUIRED", 
                "model": "CONNECTION_LOST", 
                "confidence": 0,
                "verdict": "ERROR"
            }

class SecurityManager:
    """Gestisce la validazione dei metadati e l'integrità del sistema."""
    
    @staticmethod
    def audit_image(image_input):
        """Verifica se l'immagine è valida per una perizia a pagamento."""
        try:
            img = Image.open(image_input)
            width, height = img.size
            if width < 500 or height < 500:
                return False, "Risoluzione troppo bassa per analisi sicura."
            return True, "Validazione superata."
        except:
            return False, "File immagine corrotto."
