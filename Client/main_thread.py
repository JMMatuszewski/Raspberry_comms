from TCPsocket import TCPSocket
import socket

def main_thread():

    while True:

        TCP = TCPSocket("127.0.0.1",9999)
        try:
            TCP.create_socket()
            TCP.send_msg("Msg from client main thread")
            print(TCP.rcv_msg())
        finally:
            TCP.close_socket()

        input("Press button for another interation")
