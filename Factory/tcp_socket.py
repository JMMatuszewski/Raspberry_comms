import socket
from net_socket import NetSocket

# ConcreteProduct_TCPsocket
class TCPSocket(NetSocket):
    def create_socket(self) -> socket:
        return socket.socket(socket.AF_INET, socket.SOCK_STREAM)