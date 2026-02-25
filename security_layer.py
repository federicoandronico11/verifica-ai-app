import hashlib
from datetime import datetime

class SecurityLayer:
    """Modulo per la protezione dell'integrità dei dati di scansione."""
    
    @staticmethod
    def generate_scan_hash(image_data):
        """Crea un'impronta digitale unica per ogni scansione effettuata."""
        return hashlib.sha256(image_data).hexdigest()[:16].upper()

    @staticmethod
    def validate_api_response(data):
        """Verifica che i dati ricevuti dall'IA siano conformi agli standard di Verif.ai."""
        required_keys = ["category", "brand", "model"]
        if all(key in data for key in required_keys):
            return True, "Validazione superata"
        return False, "Dati incompleti o corrotti"

    @staticmethod
    def log_security_event(event_type, details):
        """Registra eventi di sistema per scopi di audit professionale."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return f"[SEC-EVENT] {timestamp} | {event_type} | {details}"
