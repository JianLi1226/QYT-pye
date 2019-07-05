import paramiko
import time
import re


# def issue_cmd(channel, wait_time, command, hostname):
#     buff_size = 5000
#
#     channel.send((command + '\n').encode())
#     time.sleep(wait_time)
#     output = channel.recv(buff_size)
#     # while not channel.exit_status_ready():
#     #     time.sleep(wait_time)
#     #     if channel.recv_ready():
#     #         output += channel.recv(buff_size)
#
#     while not re.search(r'{0}#$'.format(hostname), output.decode().strip()):
#         channel.send(b' ')
#         output += channel.recv(buff_size)
#
#     return output.decode()




# A channel each time to issue a command and output its all response.
# To make sure that all data being received after sending a command, last two lines of the output will be taken out.
# and compare with another last two lines after sending a space, if it is the same, that means all the data has
# been received.
def issue_cmd(channel, wait_time, command):
    """Sends a command and returns its full output

    Parameters:
        channel
        wait_time
        command

    Returns:
        output
    """
    buff_size = 2048
    channel.send((command + '\n').encode())
    time.sleep(wait_time)
    output = channel.recv(buff_size)
    last_two_lines = output.decode().split('\r\n')[-2:]
    while True:
        channel.send(' '.encode())  # Send a space to get more outputs
        time.sleep(wait_time*0.4)  # Less time to wait for the response
        output += channel.recv(buff_size)
        next_last_two_lines = output.decode().strip().split('\r\n')[-2:]
        if next_last_two_lines == last_two_lines:
            break
        else:
            last_two_lines = next_last_two_lines
    return output.decode()


def qytang_multicmd(ip, username, password, cmd_list, enable='', wait_time=3, verbose=True):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh_client.connect(hostname=ip, username=username, password=password)
    except paramiko.AuthenticationException:
        print("User or password incorrect, Please try again!!!")

    cli_session = ssh_client.invoke_shell()
    time.sleep(wait_time)
    resp = cli_session.recv(2048).decode()

    # Input enable password, only when it is not in privilege mode
    if re.search(r'>', resp.strip()):
        cli_session.send('enable\n')
        time.sleep(wait_time)
        cli_session.send((enable + '\n').encode())
        resp = cli_session.recv(2048).decode()
    if re.search(r'denied',resp.strip()):
        print("Invalid enable password")

    # Input all commands
    output = ''
    for cmd in cmd_list:
        output += issue_cmd(cli_session, wait_time, cmd)
    if verbose:
        print(output)
    cli_session.send('end\n')
    ssh_client.close()


if __name__ == '__main__':
    cmd_list = ['show version', 'conf t', 'router ospf 1', 'network 1.1.1.1 0.0.0.255 area 0']
    qytang_multicmd('192.168.5.1', 'admin', 'cug@2018', enable='cisco@123', cmd_list=cmd_list)



