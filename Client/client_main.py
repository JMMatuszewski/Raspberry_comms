from protocol_lib import PROTOCOL
from networking import Connect
import threading

def network_normal():
    while True:
    
        print("Currently avalable protocols:")
        for key in PROTOCOL:
                print(f'- {key}')
        protocol = input('Please input a protocol You want to use:\n')
        #protocol = protocol.upper()
        if protocol.upper() == "Q":
                break
        elif protocol.upper() not in PROTOCOL:
                print(f'protocol "{protocol}" is not available\n')
                continue
        
        if protocol.upper() == "TCP":
            print(f'Start connection with {protocol}')
            TCPconnection = Connect(PROTOCOL['TCP']['ip'],PROTOCOL['TCP']['port'])
            TCPconnection.create_tcp_socket()
        elif protocol.upper() == "UDP":
            print(f'Start connection with {protocol}')
            TCPconnection = Connect(PROTOCOL['UDP']['ip'],PROTOCOL['UDP']['port'])
            TCPconnection.create_udp_socket()

        input("Press for another iteration")


def main():

    print("""Welcome on the client side,
          1. choose the communitaction protocol,
          2. write the message
          3. await response""")
    
    connect_loop = Connect("127.0.0.3",9997)
    t1 = threading.Thread(target=network_normal)
    t2 = threading.Thread(target=connect_loop.udp_loop)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()