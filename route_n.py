import os
import re

route_result = os.popen("route -n").read()
print(route_result)

# Method 1
for to_match in route_result.split('\n'):
    gateway = re.match(r'0.0.0.0\s*(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s*0.0.0.0.*UG', to_match)
    if gateway:
        print("Gateway is: " + gateway.groups()[0])
    # else:
    #     print('Nothing fund!')

# Method 2
# gateway_addrs = re.findall(r'0.0.0.0\s*(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s*0.0.0.0.*UG', route_result)
# # gateway_addrs = re.findall(r'0.0.0.0\s*([0-9\.]*)\s*0.0.0.0.*UG', route_result)
# for gateway_addr in gateway_addrs:
# #     print(f'Gateway is: {gateway_addr}')