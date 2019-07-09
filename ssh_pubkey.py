import paramiko

def ssh_pubkey (ip, username, password, port=22, cmd= 'route -n'):
    ssh = paramiko.SSHClient()
    #my_pri_key = r'E:\\CA-certificates\\Putty-Key\\lj_pri_openssh'
    my_pri_key = paramiko.RSAKey.from_private_key_file(r'E:\\CA-certificates\\Putty-Key\\lj_pri_openssh', password='ljkey')
    #ssh.load_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=ip, port=port, username=username, pkey=my_pri_key , timeout=5, compress=True)
    stdin,stdout,stderr = ssh.exec_command(cmd)
    x = stdout.read().decode()
    x = repr(x)
    #x = stdout.read()
    ssh.close() # Should terminate the ssh session
    return x

if __name__ == '__main__':
    # print(qytang_ssh('192.168.64.131', 'jianli', 'root'))
    print(ssh_pubkey('192.168.64.131', 'jianli', 'root',cmd='pwd'))
    # print(qytang_ssh('192.168.5.4', 'admin', 'cug@2018', cmd='show version'))