import socket
from datetime import datetime
import threading

def TCPconnect():
    while True:
        try:
            TCPserver = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # TCP protocol socket
            TCPserver.bind(('0.0.0.0', 9999))
            TCPserver.listen(5)
            client, addr = TCPserver.accept()
            print(client.recv(1024).decode())
            moment = datetime.now()
            client.send(f"Sup from TCP server {moment}".encode())
        finally:
            TCPserver.close()

def UDPconnect():
    while True:
        try:
            UDPserver = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)  # UDP protocol socket 
            UDPserver.bind(('0.0.0.0', 9998))
            data, addr = UDPserver.recvfrom(1024)
            print(data.decode())
            moment = datetime.now()
            UDPserver.sendto(f'Sup from UDP server {moment}'.encode(), addr)
        finally:
            UDPserver.close()

def UDPloop_connect():
    while True:
        try:
            UDPserver = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)  # UDP protocol socket 
            UDPserver.bind(('0.0.0.0', 9997))
            data, addr = UDPserver.recvfrom(1024)
            print(data.decode())
            moment = datetime.now()
            UDPserver.sendto(f'Sup from UDPloop server {moment}'.encode(), addr)
        finally:
            UDPserver.close()
def main():
    t1 = threading.Thread(target=TCPconnect)
    t2 = threading.Thread(target=UDPconnect)
    t3 = threading.Thread(target=UDPloop_connect)

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

if __name__ == "__main__":
    main()