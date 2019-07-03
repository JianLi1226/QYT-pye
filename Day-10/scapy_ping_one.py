from kamene.all import *

import logging
logging.getLogger("kamene.runtime").setLevel(logging.ERROR)

def qytang_ping(ip):
    ping_pkt = IP(dst=str(ip))/ICMP()
    ping_result = sr1(ping_pkt,timeout=2, verbose=False)
    if ping_result:
        return 1
    else:
        return 0

if __name__ == '__main__':
    ip = '192.168.5.1'
    result = qytang_ping(ip)
    if result:
        print(f"{str(ip):} accessible")
    else:
        print(f"{str(ip):} inaccessible")