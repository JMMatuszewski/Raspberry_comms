from abc import ABC, abstractmethod

class AbcSocket(ABC):
    @abstractmethod
    def create_socket(self):
        pass

    @abstractmethod
    def send_msg(self):
        pass

    @abstractmethod
    def rcv_msg(self):
        pass
