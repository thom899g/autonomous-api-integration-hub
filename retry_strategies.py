import random
from typing import Optional

class RetryStrategy:
    def __init__(self, max_retries=3, delay=1):
        self.max_retries = max_retries
        self.delay = delay
        
    def should_retry(self, retries_so_far: int) -> bool:
        """Determine if a retry is needed."""
        return retries_so_far < self.max_retries

def exponential_backoff(retries: int) -> float:
    """Apply exponential backoff to retry delays."""
    return min(1 + 2**retries, 30)  # Cap at 30 seconds

#