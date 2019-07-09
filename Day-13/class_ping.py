from kamene.all import *
import logging
logging.getLogger("kamene.runtime").setLevel(logging.ERROR)

class QYTPING:
    def __init__(self, ip):
        self.dst_ip = ip
        self.src_ip = None
        self.length = 100

    def one (self):
        pkt = IP(src=self.src_ip, dst=self.dst_ip) / ICMP() / (self.length * '#') # Must initialize the packet everytime
        ping_result = sr1(pkt, timeout=2, verbose=False)
        if ping_result:
            return f'{self.dst_ip} reachable!'
        else:
            return f'{self.dst_ip} unreachable!'

    def ping(self):
        for x in range(5):
            if 'unreachable' not in self.one():
                print('!', flush=True, end='')
            else:
                print('.', flush=True, end='')
        print()
        return

    def __str__(self):
        if not self.src_ip:
            return f'<{self.__class__.__name__} => dstip: {self.dst_ip}, size: {self.length}>'
        else:
            return f'<{self.__class__.__name__} => srcip: {self.src_ip}, dstip: {self.dst_ip}, size: {self.length}>'


class NewPing(QYTPING):
    def ping(self):
        for x in range(5):
            if 'unreachable' not in self.one():
                print('+', flush=True, end='')
            else:
                print('?', flush=True, end='')
        print()
        return



if __name__ == '__main__':
    ping = QYTPING('192.168.5.1')
    total_len = 70

    def print_new(word, s='-'):
        print('{0}{1}{2}'.format(s * int((70 - len(word))/2), word, s* int((70 - len(word)/2))))
    print_new('print class')
    print(ping)
    print_new('ping one for sure reachable')
    print(ping.one())
    print_new('ping five')
    ping.ping()
    print_new('set payload length')
    ping.length = 200
    print(ping)
    ping.ping()
    print_new('set src ip address')
    ping.src_ip = '192.168.1.123'
    print(ping)
    ping.ping()
    print_new('new class NewPing', '=')
    newping = NewPing('192.168.5.1')
    newping.length = 300
    print(newping)
    newping.ping()

