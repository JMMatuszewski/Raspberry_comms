from tcp_socket import TCPSocket
import socket
from protocol_lib import PROTOCOL

def tcp_thread():

    while True:

        TCP = TCPSocket(PROTOCOL['TCP'])
        TCP.create_socket()
        msg = TCP.rcv_msg()
        print(msg)
        TCP.send_msg()
        TCP.close_socket()