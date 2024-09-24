from abc_socket import AbcSocket
import socket
from datetime import datetime

class TCPSocket(AbcSocket):
    def __init__(self,port) -> None:
        self.ip = "0.0.0.0"
        self.port = port


    def create_socket(self):
        self.TCPserver = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.TCPserver.bind((self.ip,self.port))
        self.TCPserver.listen()
        self.client, addr = self.TCPserver.accept()


    def send_msg(self):
        self.client.send(f"TCP server received your message at {self.moment}".encode())


    def rcv_msg(self):
        msg = self.client.recv(1024).decode()
        self.moment = datetime.now()
        return msg


    def close_socket(self):
        self.TCPserver.close
    