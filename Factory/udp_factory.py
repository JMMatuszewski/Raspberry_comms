from net_socket import NetSocket
from factory_socket import FactorySocket
from udp_socket import UDPSocket

# ConcreteFactory_socket
class UDPFactory(FactorySocket):
    def create_socket(self) -> NetSocket:
        return UDPSocket()
    
    def create_address(self) -> str:
        ip = "127.0.0.1"
        port = 9999
        return ip,port