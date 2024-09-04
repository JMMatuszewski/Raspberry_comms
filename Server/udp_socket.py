from abc_socket import AbcSocket
import socket
from datetime import datetime

class UDPSocket(AbcSocket):
    def __init__(self,port) -> None:
        self.ip = "0.0.0.0"
        self.port = port


    def create_socket(self):
        self.UDPserver = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        self.UDPserver.bind((self.ip,self.port))


    def send_msg(self):
        self.UDPserver.sendto(f"TCP server received your message at {self.moment}".encode(), self.addr)


    def rcv_msg(self):
        msg, self.addr = self.UDPserver.recvfrom(1024)
        self.moment = datetime.now()
        return msg.decode()


    def close_socket(self):
        self.UDPserver.close
    