from matplotlib import pyplot as plt
from paramiko_ssh import qytang_ssh
import re


def collect_nf(ip, username, password):
    app_name = list()
    counters = list()
    rcvd_data = qytang_ssh(ip, username, password, cmd="show flow monitor name test-monitor cache format table")
    cleaned_rcvd_data = re.findall(r'=====\r\n([\w\W]*)', rcvd_data)[0].strip()
    for flow in cleaned_rcvd_data.split('\r\n'):
        match = re.match(r'([\w\-]* [\w\-]*)   \s+(\d+)', flow).groups()
        app_name.append(match[0])
        counters.append(int(match[1]))
    return app_name, counters


plt.style.use('fivethirtyeight')

labels, slices = collect_nf('192.168.5.1', 'admin', 'cug@2018')
print(labels)
print(slices)

plt.pie(slices, labels=labels, wedgeprops={'edgecolor':'black'}, shadow = True, autopct ="%1.1f%%")

plt.legend()
plt.tight_layout()
plt.show()
