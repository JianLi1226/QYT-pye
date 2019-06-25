import os
import re
ifconfig_result = os.popen('ifconfig ' + 'ens33').read()

# Using Re to search for IP, netmask, Broadcast address, MAC
ipv4_add = re.findall(r'inet ([0-9\.]+)', ifconfig_result)[0]
netmask = re.findall(r'netmask ([0-9\.]+)', ifconfig_result)[0]
broadcast = re.findall(r'broadcast ([0-9\.]+)', ifconfig_result)[0]
mac_addr = re.findall(r'ether ([0-9a-zA-Z:]+)', ifconfig_result)[0]

format_string = '{0:15}:{1}'

print(format_string.format('ipv4_addr', ipv4_add))
print(format_string.format('netmask', netmask))
print(format_string.format('broadcast', broadcast))
print(format_string.format('mac_addr', mac_addr))

# Find gateway IP in linux
# Define a function to find gateway address of a given interface
# Note how to use string formating method to add a variable into a regular expression.


def get_gateway_ip(interface):
    gateway_info = os.popen("ip route | grep default").read()
    # gateway_ip = re.findall(r'default via ([0-9\.]+) dev %s' % interface, gateway_info)[0]
    gateway_ip = re.findall(r'default via ([0-9\.]+) dev {}'.format(interface), gateway_info)[0]
    return gateway_ip


gateway_addr = get_gateway_ip('ens33')

# Print out the gateway address
print('\nThe gateway of interface ens33 is:' + gateway_addr + '\n')

# Ping gateway from local host
ping_result = os.popen('ping ' + gateway_addr + ' -c 1').read()

re_ping_result = re.search(r'1 packets transmitted, 1 received, 0% packet loss', ping_result)


if re_ping_result:
    print("Gateway is reachable!")
else:
    print('Gateway is unreachable!')
