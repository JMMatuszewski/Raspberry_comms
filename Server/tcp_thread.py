from tcp_socket import TCPSocket
import socket
from protocol_lib import PROTOCOL

def tcp_thread():

    # TCP = TCPSocket(PROTOCOL['TCP'])
    # TCP.create_socket()
    STATUS = False
    while True:

        try:
            # Init socket
            if not STATUS:
                TCP = TCPSocket(PROTOCOL['TCP'])
                TCP.create_socket()
                STATUS = True

            # Workspace
            msg = TCP.rcv_msg()
            print(msg)
            TCP.send_msg()
        except Exception as e:
            print(e)
            TCP.close_socket()
            STATUS = False