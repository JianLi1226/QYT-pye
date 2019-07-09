from argparse import ArgumentParser
import paramiko

def qytang_ssh (ip, username, password, port=22, cmd= 'ls'):
    ssh = paramiko.SSHClient()
    # ssh.load_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=ip, port=port, username=username, password=password, timeout=5, compress=True)
    stdin,stdout,stderr = ssh.exec_command(cmd)
    x = stdout.read().decode()
    ssh.close() # Should terminate the ssh session
    return x


if __name__ == '__main__':
    usage = 'python Simple_SSH_Client: -i ipaddr -u username -p password -c command '
    parser = ArgumentParser(usage)

    parser.add_argument('-i', '--ipaddr', dest='ipaddr', help='SSH Server', default='192.168.5.1',
                        type=str)
    parser.add_argument('-u', '--username', dest='username', help='SSH Username', default='admin',
                        type=str)
    parser.add_argument('-p', '--password', dest='password', help='SSH Password', default='cug@2018',
                        type=str)
    parser.add_argument('-c', '--command', dest='command', help='Shell Command', default='show version',
                        type=str)
    args = parser.parse_args()

    print(qytang_ssh(args.ipaddr, args.username, args.password, cmd= args.command))

