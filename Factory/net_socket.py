from abc import ABC, abstractmethod
import socket

# AbstractProduct_socket
class NetSocket(ABC):
    @abstractmethod
    def create_socket() -> socket:
        pass