import select
import socket
import signal
import pickle
import struct
import argparse


SERVER_HOST = 'localhost'
CHAT_SERVER_NAME = 'server'


# Some utilities
def send(channel, *args):
    buffer = pickle.dumps(args)
    value = socket.htonl(len(buffer))
    size = struct.pack("L", value)
    channel.send(size)
    channel.send(buffer)


def recieve(channel):
    size = struct.calcsize("L")
    size = channel.recv(size)

    try:
        size = socket.ntohl(struct.unpack("L", size)[0])
    except struct.error as e:
        return ''

    buf = b''

    while len(buf) < size:
        buf = channel.recv(size - len(buf))
    return pickle.loads(buf)[0]


class ChatServer:
    """ An example chat server using select """

    def __init__(self, port, backlog=5):
        self.clients = 0
        self.clientmap = {}
        self.outputs = []  # list output sockets
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Enable re-run of the socket
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.bind((SERVER_HOST, port))
        print(f"Listening on {port}")
        self.server.listen(backlog)

        # Catch keyboard interrupts
        signal.signal(signal.SIGINT, self.sighandler)

    def sighandler(self, signum, frame):
        """ Clean up client outputs """
        # Clost the server
        print('Closing')
        # Close existing client sockets
        for output in self.outputs:
            output.close()
        self.server.close()
    