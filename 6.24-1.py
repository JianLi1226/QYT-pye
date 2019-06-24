import re

str = '166 54a2.74f7.0326 DYNAMIC Gi1/0/11'

result = re.match(r'(\d+)\s+(\w{4}\.\w{4}\.\w{4})\s+(DYNAMIC|STATIC|STICKY)\s+([a-zA-Z0-9/]+)', str.strip()).groups()

vlan_id = 'VLAN ID'
mac = 'MAC'
type = 'Type'
itf = 'Interface'

print(f'{vlan_id:20}: {result[0]}')
print(f'{mac:20}: {result[1]}')
print(f'{type:20}: {result[2]}')
print(f'{itf:20}: {result[3]}')
