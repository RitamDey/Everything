import threading
import socketserver
import socket


SERVER_HOST = 'localhost'
SERVER_PORT = 0  # Tells kernel to pick port randomly
BUF_SIZE = 1024
ECHO_MSG = b'Hello echo Server!'


def client(ip, port, message):
    """ A client to test the server """
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, port))

    try:
        sock.sendall(message)
        response = sock.recv(BUF_SIZE).decode('utf-8')
        print(f"Client recived: {response}")
    finally:
        sock.close()


class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):
    """ An example of threaded TCP request handler """

    def handle(self):
        data = self.request.recv(1024).decode('utf-8')
        current_thread = threading.current_thread().getName()
        response = f"{current_thread}: {data}".encode('utf-8')

        self.request.sendall(response)


class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    """ Nothing to add here, inherited everything """
    pass


if __name__ == '__main__':
    # Run the server
    server = ThreadedTCPServer((SERVER_HOST, SERVER_PORT),
                               ThreadedTCPRequestHandler)

    ip, port = server.server_address

    # Start a thread with the server
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.setDaemon(True)
    server_thread.setName('Server-Thread')
    server_thread.start()

    print(f"Server loop running on thread {server_thread.name}")

    # Run clients
    client(ip, port, b'Hello from client 1')
    client(ip, port, b'Hello from client 2')
    client(ip, port, b'Hello from client 3')

    server.shutdown()
