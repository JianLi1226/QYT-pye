from paramiko_ssh import *
import re

def ssh_get_route(ip, username, pwd):
    route = qytang_ssh(ip, username, pwd, cmd= 'route -n')
    for to_match in route.split('\n'):
        gateway = re.match(r'0.0.0.0\s*(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s*0.0.0.0.*UG', to_match)
        if gateway:
            return gateway.groups()[0]
    return None # If no gateway found

if __name__ == '__main__':
    print(qytang_ssh('192.168.64.131', 'jianli', 'root'))
    print(qytang_ssh('192.168.64.131', 'jianli', 'root', cmd='pwd'))
    print('Gateway is：')
    print(ssh_get_route('192.168.64.131', 'jianli', 'root'))