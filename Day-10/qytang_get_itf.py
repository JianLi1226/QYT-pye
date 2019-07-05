from scapy_ping_one import qytang_ping
from paramiko_ssh import qytang_ssh
import paramiko
import re
import pprint

def parse_itf_info (info):
    itf_dict = dict()
    for row in info.split('\n'):
        result = re.match(r'([a-zA-z/0-9-]+)\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', row.strip())
        if result:
            itf_dict[result.groups()[0]] = result.groups()[1]
    return itf_dict


def qytang_get_if(ip_list, username, pwd):
    device_if_dict = {}
    for ip in ip_list:
        if qytang_ping(ip):
            itf_info_raw = qytang_ssh(ip, username, pwd, cmd='show ip interface brief')
            itf_info_parsed = parse_itf_info(itf_info_raw)
            device_if_dict[str(ip)] = itf_info_parsed
    return device_if_dict


devices = ['192.168.5.1', '192.168.6.55', '192.168.5.4']
pprint.pprint(qytang_get_if(devices, 'admin', 'cug@2018'), indent=4)
