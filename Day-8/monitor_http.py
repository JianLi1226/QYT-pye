import re
import os
import time

while True:
    monitor_result = os.popen('netstat -tulnp').read()
    monitor_result_list = monitor_result.split('\n')
    flag = 0 # set a flag to indicate if the while loop should continue
    for row in monitor_result_list:
        if re.match(r'tcp.*0.0.0.0:80.*LISTEN',row):
            flag = 1
            break
    if flag:
        print('HTTP (TCP/80) service has already been launched')
        break
    else:
        print('1 second later to restart monitoring process')
        time.sleep(1)
