import socket
from datetime import datetime
import threading
from tcp_thread import tcp_thread
from udp_thread import udp_thread


def main():

    print("Server is running")

    t0 = threading.Thread(target=tcp_thread)
    t1 = threading.Thread(target=udp_thread)

    t0.start()
    t1.start()

    t0.join()
    t1.join()


if __name__ == "__main__":
    main()