from django.apps import AppConfig, apps
from django.urls import get_resolver

import requests as r

class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    def ready(self):
        service = {
            'name':     self.name,
            'port':     8002,
            'routes':   [],
        }
        routes = get_resolver().reverse_dict.values()
        url = 'http://192.168.199.9:8001/services/'
        for route in routes:
            service['routes'].append({
                'path': route[0][0][0],
            })

        try:
            req = r.post(url, json=service)
        except Exception as err:
            print('Can\'t connect to registry server!')
