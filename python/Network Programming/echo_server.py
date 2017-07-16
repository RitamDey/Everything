import os
import socket
import threading
import socketserver


SERVER_HOST = 'localhost'
SERVER_PORT = 0  # Tells kernel to pick port randomly
BUF_SIZE = 1024
ECHO_MSG = b'Hello echo Server!'


class ForkedClient():
    def __init__(self, ip, port):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((ip, port))

    def run(self):
        current_process_id = os.getpid()
        print('PID %s. Sending message: %s' % (current_process_id, ECHO_MSG))
        sent_data_length = self.socket.send(ECHO_MSG)
        print("Sent: %d characters" % sent_data_length)

        response = self.socket.recv(BUF_SIZE)
        print("PID %s recieved %s" % (current_process_id, response[5:]))

    def shutdown(self):
        self.socket.close()


class ForkingServerRequestHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data = self.request.recv(BUF_SIZE)
        current_process_id = os.getpid()

        response = "%s: %s" % (current_process_id, data)
        response = bytes(response, 'utf-8')
        print("Server sending response [pid: data]: %s" % response)

        self.request.send(response)
        return


class ForkingServer(socketserver.ForkingMixIn, socketserver.TCPServer):
    """ Nothing to add here. Inhereted everything """
    pass


def main():
    # Launch the server
    server = ForkingServer((SERVER_HOST, SERVER_PORT), ForkingServerRequestHandler)
    ip, port = server.server_address  # Getting the port number
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.setDaemon(True)
    server_thread.start()

    print('Server loop running PID: %s' % os.getpid())

    # Launch the client
    client1 = ForkedClient(ip, port)
    client1.run()

    client2 = ForkedClient(ip, port)
    client2.run()

    # Clean them up
    server.shutdown()
    client1.shutdown()
    client2.shutdown()
    server.socket.close()


if __name__ == '__main__':
    main()
