from scapy.all import *

import threading as th

class OsDetection:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.result = {
            'Windows':          0,
            'Linux':            0,
            'FreeBSD':          0,
            'MacOS':            0,
            'Solaris':          0,
            'Other':            0,
        }

    def run(self):
        self.__window_size_method()
        self.__ttl_method()
        return self.result

    def __window_size_method(self):
        ip = IP(dst=self.host)
        tcp = TCP(dport=self.port, flags='S')
        pkt = ip/tcp
        ans = sr1(pkt, timeout=1, verbose=False)
        if ans:
            win_size = ans[TCP].window
            print(win_size)

    def __ttl_method(self):
        ip = IP(dst=self.host)
        tcp = TCP(dport=self.port, flags='S')
        pkt = ip/tcp

        ans = sr1(pkt, timeout=1, verbose=False)
        if ans:
            ttl = ans[IP].ttl
            print(ttl)
            if ttl == 128:
                self.result['Windows'] += 1
            elif ttl == 64:
                self.result['Linux'] += 1
                self.result['MacOS'] += 1
                self.result['FreeBSD'] += 1
            elif ttl == 255:
                self.result['Solaris'] += 1
            else:
                pass
