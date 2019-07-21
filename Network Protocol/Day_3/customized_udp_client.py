# -*- coding: utf-8 -*-
import socket
import struct
import pickle
from hashlib import md5


def udp_send_data(ip, port, data_list):
    address = (ip, port)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    version = 1
    pkt_type = 1
    seq_id = 1

    for x in data_list:
        send_data = pickle.dumps(x)

        # Version field - 2 bytes
        version_field = struct.pack("!H", version)

        # Type field - 2 bytes
        type_filed = struct.pack("!H", pkt_type)

        # ID field - 4 bytes
        id_field = struct.pack("!i", seq_id)

        # Length field - 4 bytes, only the length of payload
        udp_length = len(send_data)
        length_field = struct.pack("!i", udp_length)

        # Calculate Md5 of udp packet, original data includes header and data
        m = md5()
        m.update(version_field + type_filed + id_field + length_field + b"\x00" * 16 + send_data)
        udp_checksum = m.digest()

        udp_pkt = version_field + type_filed + id_field + length_field + udp_checksum + send_data
        s.sendto(udp_pkt, address)

        seq_id += 1
    s.close()


if __name__== "__main__":
    user_data = ["乾颐堂", [1, 'qytang', 3], {"qytang":1, "test":3}]
    udp_send_data("192.168.64.131", 6666, user_data)
