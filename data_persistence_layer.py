import hashlib
import json
import os

class DataPersistence:
    """Sistema di cache intelligente per ridurre i costi API."""
    
    def __init__(self, cache_dir=".cache"):
        self.cache_dir = cache_dir
        if not os.path.exists(cache_dir):
            os.makedirs(cache_dir)

    def _get_hash(self, image_bytes):
        return hashlib.md5(image_bytes).hexdigest()

    def check_cache(self, image_bytes):
        cache_path = os.path.join(self.cache_dir, self._get_hash(image_bytes))
        if os.path.exists(cache_path):
            with open(cache_path, 'r') as f:
                return json.load(f)
        return None

    def save_to_cache(self, image_bytes, result):
        cache_path = os.path.join(self.cache_dir, self._get_hash(image_bytes))
        with open(cache_path, 'w') as f:
            json.dump(result, f)
