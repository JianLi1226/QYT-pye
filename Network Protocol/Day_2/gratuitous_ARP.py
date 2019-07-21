# -*- coding=utf-8 -*-
import logging
from Day_1.get_mac_netifaces import get_mac_address
from Day_1.scapy_iface import scapy_iface
from Day_1.get_ifname import get_ifname
logging.getLogger("kamene.runtime").setLevel(logging.ERROR)  # 清除报错
from kamene.all import *
import signal
import time


def arp_gratuitous(ip, ifname):
    localmac = get_mac_address(ifname)
    broadcast = 'ff:ff:ff:ff:ff:ff'
    signal.signal(signal.SIGINT, sigint_handler)
    while True:
        sendp(Ether(src=localmac, dst=broadcast) / ARP(op=2, hwsrc=localmac, psrc=ip, hwdst=broadcast, pdst=ip),
              iface=scapy_iface(ifname), verbose=False)

        print(f"Send Gratuitous ARP to claim host: {ip} has hardware address: {localmac}")
        time.sleep(1)


def sigint_handler(signum, frame):  # 定义处理方法
    print("\n停止发送！！！")
    sys.exit(0)

if __name__ == "__main__":
    arp_gratuitous('192.168.55.1', 'ens33')