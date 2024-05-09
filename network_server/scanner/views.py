from fastapi import Request, Response
from scapy.all import *

import threading as th
import os

async def ping(request: Request):
    host = request.query_params.get('host', None)
    if not host:
        return Response(status_code=400)
    res = sr1(IP(dst=host) / ICMP(), timeout=1, verbose=False)
    if res:
        return Response(status_code=200)
    return Response(status_code=404)
