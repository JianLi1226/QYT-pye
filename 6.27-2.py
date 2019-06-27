import re
import string
port_list = ['eth 1/101/1/42','eth 1/101/1/26','eth 1/101/1/23','eth 1/101/1/7',
             'eth 1/101/2/46','eth 1/101/1/34','eth 1/101/1/18','eth 1/101/1/13',
             'eth 1/101/1/32','eth 1/101/1/25','eth 1/101/1/45','eth 1/101/2/8']

port_list.sort(key=lambda x:(int(x[11:].replace('/',''))+int(x[4:11].replace('/','')*100)))
print(port_list)
#test vcs