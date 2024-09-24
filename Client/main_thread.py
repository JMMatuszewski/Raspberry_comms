from tcp_socket import TCPSocket
from udp_socket import UDPSocket
import socket
from protocol_lib import PROTOCOL
import msvcrt
import time
from pynput import keyboard
#from pynput.keyboard import Key

def main_thread():

    while True:
        
        ### PROTOCOL UI ###
        print("Currently avalable protocols:")
        for key in PROTOCOL:
                print(f'- {key}')
        protocol = input('Please input a protocol You want to use:\n')
        # protocol = "udp" // TEST
        protocol = protocol.upper()
        if protocol == "Q":
                break
        elif protocol not in PROTOCOL:
                print(f'protocol "{protocol}" is not available\n')
                continue

        ### KEY LISTENER ###
        #msg = input("Please write a short message:\n")
        print("Make a move: ")
        #if key 
        #char = str(msvcrt.getch().decode())
        char keyboard.Key.
        print(ord(char))

        #with keyboard.Listener()










        #####################################################################

        # Basic way for chosing method of communication - for rework later.

        if protocol == 'TCP':
            try:
                TCP = TCPSocket(PROTOCOL[protocol]['ip'],PROTOCOL[protocol]['port'])
                TCP.create_socket()
                TCP.send_msg(char) #msg
                print(TCP.rcv_msg())
            finally:
                TCP.close_socket()
        if protocol == 'UDP':
            try:
                UDP = UDPSocket(PROTOCOL[protocol]['ip'],PROTOCOL[protocol]['port'])
                UDP.create_socket()
                UDP.send_msg(char)
                #time.sleep(1)
                print(UDP.rcv_msg())
            finally:
                UDP.close_socket()
                
        # TESTING STOPPER
        # input("Press button for another interation")
