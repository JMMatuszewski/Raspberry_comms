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
        except ConnectionRefusedError:
            print("Socket was not created")






        #event_service = EventService()
        #key = event_service.listener_start()
        #print(key)
        # while True:
        #     key = event_service.key_out()
        #     print(key)


        #msg = input("Please write a short message:\n")
        #print("Make a move: ")
        #if key 
        #char = str(msvcrt.getch().decode())
        #char keyboard.Key.
        #print(ord(char))

        #with keyboard.Listener()
    # print("""Welcome on the client side,
    #       1. choose the communitaction protocol,
    #       2. write the message
    #       3. await response""")

    # t0 = threading.Thread(target=main_thread)

    # t0.start()

    # t0.join()


if __name__ == "__main__":
    main()