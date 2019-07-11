from paramiko_ssh import qytang_ssh
import re
import string
import hashlib
import time


def get_config(ip, username, pwd):
    try:
        cfg = qytang_ssh(ip, username, pwd, cmd='show running')
        # Add more details into filters, in case 'end' appears in the other lines
        cfg_parsed = re.findall(r'(hostname[\w\W]*\r\nend)', cfg.strip())[0]
        return cfg_parsed
    except Exception:
        return


def get_md5_val(input):
    m = hashlib.md5()
    m.update(input.encode())
    return m.hexdigest()



def monitor_cfg_chg(ip, username, pwd):
    cur_cfg_md5 = get_md5_val(get_config(ip, username, pwd))
    while True:
        time.sleep(5)
        next_cfg_md5 = get_md5_val(get_config(ip, username, pwd))
        if cur_cfg_md5 == next_cfg_md5:
            print(cur_cfg_md5)
            cur_cfg_md5 = next_cfg_md5
        else:
            print(next_cfg_md5)
            print('MD5 value changed！')
            break


if __name__ == '__main__':
    monitor_cfg_chg('192.168.5.4', 'admin', 'cug@2018')


