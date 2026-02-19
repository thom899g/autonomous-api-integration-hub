import time

class PerformanceMetrics:
    def __init__(self):
        self.metrics = {}
        
    def record_response_time(self, api_name, response_time):
        """Record the response time of an API call."""
        if api_name not in self.metrics:
            self.metrics[api_name] = []
        self.metrics[api_name].append(response_time)
    
    def get_median_response_time(self, api_name):
        """Get the median response time for an API."""
        times = self.metrics.get(api_name, [])
        if not times:
            return 0
        return sorted(times)[len(times)//2]