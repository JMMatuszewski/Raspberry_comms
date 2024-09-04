import socket
import time

class Connect:
    def __init__(self,ip,port) -> None:
        self.ip = ip
        self.port = port
        #self.protocol = protocol

    def create_tcp_socket(self) -> None:
        self.TCPclient = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.TCPclient.connect((self.ip,self.port))
        print("connection established")
        self.TCPclient.send("sent from TCP client".encode())
        print(self.TCPclient.recv(1024).decode())

    def create_udp_socket(self) -> None:
        self.UDPclient = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.UDPclient.sendto("Sup from UDP client".encode(),(self.ip, self.port))
        data, addr = self.UDPclient.recvfrom(1024)
        print(data.decode())

    def udp_loop(self):
        while True:
            print("loop iteration")
            UDPloop = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            UDPloop.sendto("Sup from UDPloop client".encode(),(self.ip, self.port))
            time.sleep(1)
            data, addr = UDPloop.recvfrom(1024)
            print(data.decode())
