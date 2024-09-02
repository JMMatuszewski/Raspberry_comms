from abc import ABC, abstractmethod
from net_socket import NetSocket

# AbstractFactory_socket
class FactorySocket(ABC):
    @abstractmethod
    def create_socket(self) -> NetSocket:
        pass

    @abstractmethod
    def create_address(self) -> str:
        pass