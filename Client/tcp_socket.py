from abc_socket import AbcSocket
import socket

class TCPSocket(AbcSocket):
    def __init__(self,ip,port) -> None:
        self.ip = ip
        self.port = port


    def create_socket(self):
        self.TCPclient = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.TCPclient.connect((self.ip,self.port))


    def send_msg(self,msg):
        self.TCPclient.send(msg.encode())


    def rcv_msg(self):
        msg = self.TCPclient.recv(1024).decode()
        return msg


    def close_socket(self):
        self.TCPclient.close
    