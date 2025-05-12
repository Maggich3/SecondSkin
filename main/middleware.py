from django.core.cache import cache

class ClearCacheMiddleware:
    def __init__(self, get_response):  # правильно: __init__
        self.get_response = get_response

    def __call__(self, request):       # правильно: __call__
        cache.clear()  # Очистка всего кэша
        response = self.get_response(request)
        return response
