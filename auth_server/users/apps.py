from django.apps import AppConfig, apps
from django.urls import get_resolver

import requests as r

class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'
    executed = False

    def ready(self):
        if self.executed:
            return

        service = {
            'name':     self.name,
            'port':     8002,
            'routes':   [],
        }
        routes = get_resolver().reverse_dict.values()
        url = 'http://localhost:8001/service/'
        for route in routes:
            service['routes'].append({
                'path': route[0][0][0],
            })

        req = r.post(url, json=service)

        self.executed = True
