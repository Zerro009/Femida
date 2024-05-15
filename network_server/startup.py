from fastapi import FastAPI

import requests as r
import os

def startup(app: FastAPI):
    try:
        service = {
            'name':     'scanner',
            'port':     8000,
            'routes':   [route.path for route in app.router.routes[4:]]
        }
        url = 'http://192.168.199.9:8001/services/'
        req = r.post(url, json=service)
    except Exception as err:
        print('Can\'t connect to registry server!')
