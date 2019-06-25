import re

str = 'TCP server 172.16.1.101:443 localserver 172.16.66.1:53710, idle 0:01:09, bytes 27575949, flags UIO'

result = re.match(r'(\w+) server (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{1,5}) ' \
                  'localserver (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{1,5}), '\
                  'idle (\d+):(\d+):(\d+), bytes (\d+), flags (\w+)', str.strip()).groups()

# print('protocol'.ljust(23, ' ') + ': ' + result[0])
# print('server'.ljust(23, ' ') + ': ' + result[1])
# print('localserver'.ljust(23, ' ') + ': ' + result[2])
# print('idle'.ljust(23, ' ') + ': ' + result[3] + ' hour ' + result[4] + ' minute ' + result[5] + ' second')
# print('bytes'.ljust(23, ' ') + ': ' + result[6])
# print('flags'.ljust(23, ' ') + ': ' + result[7])

print('%-23s: %s'%("protocol", result[0]))
print(f'{"server":<23}: {result[1]}')



