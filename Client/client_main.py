from protocol_lib import PROTOCOL
from event_service import EventService
from pynput import keyboard
from event_service import EventService
#import threading
#from main_thread import main_thread
      
def main():

    while True:

        ### PROTOCOL UI ###
        print("Currently avalable protocols:")
        for key in PROTOCOL:
            print(f'- {key}')
        protocol = input('Please input a protocol You want to use:\n')
        # protocol = "udp" # TEST
        protocol = protocol.upper()
        if protocol == "Q":
            break
        elif protocol not in PROTOCOL:
            print(f'protocol "{protocol}" is not available\n')
            continue

        ### KEY LISTENER ###
        try:
            service = EventService(protocol)
            service.listener_start()
        #except ConnectionRefusedError:
        except Exception as e:
            #print(e)
            print("Connection error")


if __name__ == "__main__":
    main()