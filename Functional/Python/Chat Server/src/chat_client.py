import socket

addr = (input("Enter a server's IP: "), 8081)
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)


def connect():
    """
    This function connects to a server
    """
    soc.connect(addr)
    msg = soc.recv(1024).decode("utf-8")
    print(msg)


def chat():
    """
    The chat function
    """
    connect()
    try:
        while True:
            soc.sendall(input("Enter message: ").encode('utf-8'))
            data = soc.recv(204800)
            print(data.decode('utf-8'))
    except KeyboardInterrupt:
        exit(0)


if __name__ == '__main__':
    chat()
