import logging
from datetime import datetime

class Monitor:
    def __init__(self, logger=None):
        self.logger = logger or logging.getLogger(__name__)
        
    def log_connection_attempt(self, api_name, status):
        """Log an API connection attempt."""
        self.logger.info(f"{datetime.now()}: Attempted connection to {api_name} - {status}")