from fastapi import FastAPI

import requests as r
import os

PROD = os.getenv('PROD')
print(PROD)

def startup(app: FastAPI):
    try:
        service = {
            'name':     'scanner',
            'port':     8003,
            'routes':   [{'path': route.path} for route in app.router.routes[4:]]
        }
        url = None
        if PROD:
            url = 'http://%s:%s/services/' % (os.getenv('REGISTRY_SERVER_HOST'), os.getenv('REGISTRY_SERVER_PORT'))
        else:
            url = 'http://localhost:8001/services/'
        req = r.post(url, json=service)
    except Exception as err:
        print('Can\'t connect to registry server!')
