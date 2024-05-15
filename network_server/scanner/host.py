from scapy.all import *

import threading as th

class Host:
    def __init__(self, ipv4):
        self.ipv4 = ipv4

class HostDetection:
    def __init__(self, ipv4):
        self.ipv4 = ipv4

    def __ping_host(self, ipv4, hosts,):
        try:
            pkt = IP(dst=ipv4) / ICMP()
            ans = sr1(pkt, timeout=2, verbose=False)
            print('%s - %s' % (ipv4, ans))
            if ans:
                hosts.append(Host(ipv4))
        except Exception as e:
            return None

    def ping(self):
        hosts = []
        threads = []
        pkt = IP(dst=self.ipv4) / ICMP()
        network, mask = self.ipv4.split('/')
        network = network[:network.rfind('.')]
        end = 2 ** (32 - int(mask))

        for i in range(1, end - 1):
            ipv4 = '%s.%s' % (network, i)
            thread = th.Thread(target=self.__ping_host, args=(ipv4, hosts), daemon=True)
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        return hosts
