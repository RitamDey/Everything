import socket
from sys import exit

addr = ("", 8081)
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
soc.bind(addr)


def listen():
    """
    This function just waits for a client to join the server
    """
    soc.listen()
    global conn, client
    conn, client = soc.accept()
    conn.sendall(b"Welcome to Awesomely Awful Chat Server")
    print("Connected Client address " + str(client[0]) + ":" + str(client[1]))


def sender():
    """
    The message sender
    """
    try:
        while True:
            conn.send(input("Enter message: ").encode("utf-8"))
            receiver()
    except KeyboardInterrupt:
        exit(0)


def receiver():
    """
    The message receiver
    """
    print(conn.recv(204800).decode("utf-8"))


if __name__ == '__main__':
    listen()
    sender()
    receiver()
