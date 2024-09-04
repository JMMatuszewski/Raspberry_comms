from protocol_lib import PROTOCOL
import threading
from main_thread import main_thread

def main():

    print("""Welcome on the client side,
          1. choose the communitaction protocol,
          2. write the message
          3. await response""")

    t0 = threading.Thread(target=main_thread)

    t0.start()

    t0.join()


if __name__ == "__main__":
    main()