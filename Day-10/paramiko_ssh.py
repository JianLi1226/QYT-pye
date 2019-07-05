import paramiko

def qytang_ssh (ip, username, password, port=22, cmd= 'ls'):
    ssh = paramiko.SSHClient()
    # ssh.load_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=ip, port=port, username=username, password=password, timeout=5, compress=True)
    stdin,stdout,stderr = ssh.exec_command(cmd)
    x = stdout.read().decode()
    x = repr(x)
    #x = stdout.read()
    ssh.close() # Should terminate the ssh session
    return x

if __name__ == '__main__':
    # print(qytang_ssh('192.168.64.131', 'jianli', 'root'))
    # print(qytang_ssh('192.168.64.131', 'jianli', 'root',cmd='pwd'))
    print(qytang_ssh('192.168.5.4', 'admin', 'cug@2018', cmd='show version'))