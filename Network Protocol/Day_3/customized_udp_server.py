#!/usr/bin/python3
# -*- coding: utf-8 -*-
import socket
import sys
import pickle
import struct
from hashlib import md5


address = ("192.168.64.1", 6666)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(address)

print('UDP服务器就绪!等待客户数据!')
while True:
    try:
        receive_source_data = s.recvfrom(2048)
        data, addr = receive_source_data
        # 如果客户发来空数据,就退出循环
        if not data:
            print("客户端退出!")
            break

        # Version field - 2 bytes
        version_byte = data[0:2]
        version = struct.unpack("!H", version_byte)[0]

        # Type field - 2 bytes
        type_byte =  data[2:4]
        type = struct.unpack("!H", type_byte)[0]

        # # ID field - 4 bytes
        id_byte = data[4:8]
        seq_id = struct.unpack("!i", id_byte)[0]

        # # Length field - 4 bytes
        len_byte = data[8:12]
        length = struct.unpack("!i", len_byte)[0]

        # Use hex() to convert byte object into a hex string
        md5_recv = data[12:28].hex()
        #print("received md5:" + md5_recv)
        # Calculate Md5 of udp packet, original data includes header and data
        m = md5()
        m.update(data[:12] + b"\x00"*16 + data[28:])
        md5_value = m.hexdigest()
        # print("caled md5:" + md5_value)


        if md5_recv == md5_value:
            print('=' * 80)
            print("{0:<30}:{1:<30}".format("数据来自于", str(addr)))
            print("{0:<30}:{1:<30}".format("数据序号为", seq_id))
            print("{0:<30}:{1:<30}".format("数据长度为", length))
            # Have to specify the encoding scheme for loads() to handel chinese characters
            print("{0:<30}:{1:<30}".format("数据内容为", str(pickle.loads(data[28:], encoding='utf-8'))))
    except KeyboardInterrupt:
        sys.exit()

s.close()
