from scapy.all import *

from .fingerprint import *

import threading as th

def scan_port(host, port, json, F=False):
    result = sr1(IP(dst=host) / TCP(dport=port, flags="S"), timeout=1, verbose=False)
    if result and result[TCP].flags == 18:
        json[port] = dict()
        json[port]['status'] = 'open'
        if F:
            pass

def scan_ports(host, from_p, to_p, F=False):
    result = dict()
    threads = []

    for port in range(from_p, to_p + 1):
        t = th.Thread(target=scan_port, args=(host, port, result, F))
        threads.append(t)

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    if F:
        pass

    return result


