import time
from datetime import datetime

class SystemMonitor:
    """Monitora le prestazioni dell'IA e i tempi di risposta dei server Google."""
    
    def __init__(self):
        self.start_time = None
        self.logs = []

    def start_timer(self):
        self.start_time = time.time()

    def stop_timer(self, action_name):
        if self.start_time:
            duration = round(time.time() - self.start_time, 2)
            timestamp = datetime.now().strftime("%H:%M:%S")
            log_entry = f"[{timestamp}] {action_name}: {duration}s"
            self.logs.append(log_entry)
            return duration
        return 0

    def get_summary(self):
        return self.logs[-5:] # Restituisce gli ultimi 5 eventi
