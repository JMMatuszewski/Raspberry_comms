from udp_socket import UDPSocket
import socket
from protocol_lib import PROTOCOL

def udp_thread():

    while True:

        TCP = UDPSocket(PROTOCOL['UDP'])
        TCP.create_socket()
        msg = TCP.rcv_msg()
        print(msg)
        TCP.send_msg()
        TCP.close_socket()