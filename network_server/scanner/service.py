from scapy.all import *

import threading as th

class ServiceDetection:
    def __init__(self, ipv4, port):
        self.ipv4 = ipv4
        self.port = port

    def run(self):
        pass
