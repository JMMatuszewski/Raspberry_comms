from abc_socket import AbcSocket
import socket
from protocol_lib import PROTOCOL

class UDPSocket(AbcSocket):
    def __init__(self,ip,port) -> None:
        self.ip = ip
        self.port = port


    def create_socket(self):
        self.UDPclient = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)


    def send_msg(self,msg):
        self.UDPclient.sendto(msg.encode(),(self.ip,self.port))


    def rcv_msg(self):
        msg, self.addr = self.UDPclient.recvfrom(1024)
        return msg.decode()


    def close_socket(self):
        self.UDPclient.close()
    