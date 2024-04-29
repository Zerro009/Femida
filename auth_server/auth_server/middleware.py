from django.core.exceptions import MiddlewareNotUsed
from django.conf import settings

class StartupMiddleware:
    def __init__(self):
        print("!!!!!!!")
        raise MiddlewareNotUsed('Startup completed!')
