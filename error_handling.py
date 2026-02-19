class APIConnectionError(Exception):
    """Raised when an API connection fails."""
    
    def __init__(self, message, status_code=None, details=None):
        super().__init__(message)
        self.status_code = status_code
        self.details = details

def handle_api_errors(func):
    """Decorator for handling API-related errors."""
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except APIConnectionError as e:
            # Log error and retry logic here
            raise
    return wrapper