from tcp_socket import TCPSocket
from udp_socket import UDPSocket
import socket
from protocol_lib import PROTOCOL

def main_thread():

    while True:
        
        print("Currently avalable protocols:")
        for key in PROTOCOL:
                print(f'- {key}')
        protocol = input('Please input a protocol You want to use:\n')
        protocol = protocol.upper()
        if protocol == "Q":
                break
        elif protocol not in PROTOCOL:
                print(f'protocol "{protocol}" is not available\n')
                continue
        msg = input("Please write a short message:\n")
        

        # Basic way for chosing method of communication - for rework later.

        if protocol == 'TCP':
            try:
                TCP = TCPSocket(PROTOCOL[protocol]['ip'],PROTOCOL[protocol]['port'])
                TCP.create_socket()
                TCP.send_msg(msg)
                print(TCP.rcv_msg())
            finally:
                TCP.close_socket()
        if protocol == 'UDP':
            try:
                UDP = UDPSocket(PROTOCOL[protocol]['ip'],PROTOCOL[protocol]['port'])
                UDP.create_socket()
                UDP.send_msg(msg)
                print(UDP.rcv_msg())
            finally:
                UDP.close_socket()
                

        input("Press button for another interation")
