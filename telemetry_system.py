import time
from datetime import datetime

class TelemetrySystem:
    """Sistema avanzato di monitoraggio delle prestazioni API."""
    
    def __init__(self):
        self.session_start = datetime.now()
        self.performance_logs = []

    def record_latency(self, start_time):
        """Calcola il tempo di risposta del server Google."""
        latency = round(time.time() - start_time, 3)
        self.performance_logs.append({
            "timestamp": datetime.now().strftime("%H:%M:%S"),
            "latency_seconds": latency
        })
        return latency

    def get_session_report(self):
        """Genera un sommario tecnico della sessione."""
        if not self.performance_logs:
            return "Nessun dato registrato."
        avg_lat = sum(l['latency_seconds'] for l in self.performance_logs) / len(self.performance_logs)
        return f"Media latenza: {avg_lat}s | Totale scansioni: {len(self.performance_logs)}"
