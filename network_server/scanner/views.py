from fastapi import Request, Response
from fastapi.responses import JSONResponse
from scapy.all import *

from .tcp import *
from .host import HostDetection
from .os import OsDetection

import threading as th


'''
async def ping(request: Request):
    host = request.query_params.get('host', None)
    if not host:
        return Response(status_code=400)
    res = sr1(IP(dst=host) / ICMP(), timeout=1, verbose=False)
    if res:
        return Response(status_code=200)
    return Response(status_code=404)
'''

'''
async def ping_view(request: Request):
    ipv4 = request.query_params.get('ipv4', None)
    mask = request.query_params.get('mask', None)
    if not ipv4:
        return Response(status_code=400)
    pkt = Ether() / IP(dst=host) / ICMP()
    res = srp1(pkt, timeout=2, verbose=False)
    if res:
        return Response(status_code=200)
    return Response(status_code=404)
'''
async def ping_view(request: Request):
    ipv4 = request.query_params.get('ipv4', None)
    if not ipv4:
        return Response(status_code=400)
    return HostDetection(ipv4).ping()

async def tcp_scan_view(request: Request):
    host = request.query_params.get('host', None)
    from_p = int(request.query_params.get('from', None))
    to_p = int(request.query_params.get('to', None))
    F = bool(request.query_params.get('F', None))

    if not host:
        return Response(status_code=400)

    result = scan_ports(host, from_p, to_p, F)

    return JSONResponse(
        content=result
    )

async def os_scan_view(request: Request):
    host = request.query_params.get('host', None)
    port = request.query_params.get('port', None)

    if not host:
        return Response(status_code=400)

    '''
    result = {}
    temp = 0x0
    ans, unans = srloop(IP(dst=host) / TCP(dport=port, flags='S'), count=10, verbose=False)
    for s, r in ans:
        temp = r[TCP].seq - temp
        print(temp)
    '''
    result = {
        'Windows':      0,
        'GNU/Linux':   0,
        'MacOS':        0,
        'Other':        0,
    }

    if not port:
        port = RandShort()

    return JSONResponse(
        content=OsDetection(host, int(port)).run()
    )
