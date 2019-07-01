import re

asa_conn = "TCP Student 192.168.189.167:32806 Teacher 137.78.5.128:65247, " \
           "idle 0:00:00, bytes 74, flags UIO\n TCP Student 192.168.189.167:80 " \
           "Teacher 137.78.5.128:65233, idle 0:00:03, bytes 334516, flags UIO\n   TCP Student 192.168.189.167:80 " \
           "Teacher 137.78.5.128:652, idle 0:00:03, bytes 3516, flags UIO"
# print(re.match(r'\w*\s\w*\s(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{1,5})\s\w+\s(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{1,5}).*bytes (\d+), flags (\w*)', str).groups())


sessions_list = list()
session_dict = dict()

for session in asa_conn.split('\n'):
    # session_parsed = re.match(r'\w*\s\w*\s(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{1,5})\s\w+\s'
    #                           r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{1,5})'
    #                           r'.*bytes (\d+), flags (\w*)', session.strip()).groups()
    # Try findall()
    session_parsed = re.findall(r'\w* \w* (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{1,5}) \w+ '
                              r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{1,5})'
                              r'.*bytes (\d+), flags (\w*)', session.strip())

    #print(session_parsed)
    session_key = session_parsed[0][0:4] # groups() returns a tuple of subgroups, and tuple can be key of a dict.
    session_val = session_parsed[0][4:6]
    # session_dict = dict() # Have to create a new dict in each loop
    session_dict[session_key] = session_val
    #session_dict = {session_key:session_val}
    #
    # sessions_list.append(session_dict)

# for ses_dict in sessions_list:
#     for key, val in ses_dict.items():
#         print(f'{"src_ip":^10}:{key[0]:^20}|{"src_port":^10}:{key[1]:^10}|'
#               f'{"dst_ip":^10}:{key[2]:^20}|{"dst_port":^10}:{key[3]:^10}')
#         print(f'{"bytes":^10}:{val[0]:^20}|{"flags":^10}:{val[1]:^10}')
#         print("="*110)


for key, val in session_dict.items():
    print(f'{"src_ip":^10}:{key[0]:^20}|{"src_port":^10}:{key[1]:^10}|'
            f'{"dst_ip":^10}:{key[2]:^20}|{"dst_port":^10}:{key[3]:^10}')
    print(f'{"bytes":^10}:{val[0]:^20}|{"flags":^10}:{val[1]:^10}')
    print("="*110)
