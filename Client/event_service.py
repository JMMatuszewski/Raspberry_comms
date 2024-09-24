from input_lib import INPUT
from pynput import keyboard
#from queue import Queue
from udp_socket import UDPSocket
from tcp_socket import TCPSocket
from protocol_lib import PROTOCOL

class EventService:

    def __init__(self,protocol) -> None:
        # init socket
        self.protocol = protocol.upper()
        if self.protocol == 'UDP':
            self.sock = UDPSocket(PROTOCOL[self.protocol]['ip'],PROTOCOL[self.protocol]['port'])
        if self.protocol == 'TCP':
            self.sock = TCPSocket(PROTOCOL[self.protocol]['ip'],PROTOCOL[self.protocol]['port'])
        self.sock.create_socket()

        # self.keys = []
        # self.queue = Queue()

    
    def listener_start(self):
        with keyboard.Listener(
                on_press=self.on_press) as listener:
            listener.join()


    def on_press(self,key):
        # try:
            #self.sock.create_socket()
        self.sock.send_msg(str(key))
            #if self.protocol == 'TCP':
        s = self.sock.rcv_msg()
        print(s)
            #self.sock.close_socket()
        # except Exception as e:
        #     print(e)
        # print(key)

        #self.queue.put(key)

    
    def on_release(self,key):
        pass


    # def key_out(self):
    #     return self.queue.get()