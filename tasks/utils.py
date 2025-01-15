from django.core.cache import cache
from functools import wraps
from rest_framework.response import Response

def cache_response(timeout=15):
    def decorator(func):
        @wraps(func)
        def wrapped(viewset, request, *args, **kwargs):
            # Создание уникального ключа для кэширования, используя путь запроса
            cache_key = f"cache_{request.get_full_path()}"
            # Проверка, есть ли кэшированный ответ
            cached_data = cache.get(cache_key)
            if cached_data:
                return Response(cached_data)  # Если данные есть в кэше, возвращаются

            # Если данных нет в кэше, вызывается оригинальная функция
            response = func(viewset, request, *args, **kwargs)

            # Проверка, что response был полностью обработан
            if isinstance(response, Response):
                # Кэширование результата на заданный промежуток времени
                cache.set(cache_key, response.data, timeout)

            return response

        return wrapped
    return decorator
