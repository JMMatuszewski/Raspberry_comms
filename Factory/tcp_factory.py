from net_socket import NetSocket
from factory_socket import FactorySocket
from tcp_socket import TCPSocket

# ConcreteFactory_socket
class TCPFactory(FactorySocket):
    def create_socket(self) -> NetSocket:
        return TCPSocket()
    
    def create_address(self) -> str:
        ip = "127.0.0.2"
        port = 9998
        return ip,port