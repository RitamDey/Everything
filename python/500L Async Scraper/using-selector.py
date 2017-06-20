from selectors import DefaultSelector, EVENT_WRITE
from socket import socket


# This selector will use the selector in the system
selector = DefaultSelector()


sock = socket()
sock.setblocking(False)  # Set to non-blocking
try:
    sock.connect(('xkcd.com', 80))
except BlockingIOError:
    pass


def loop():
    while True:
        events = selector.select()
        for event_key, event_mask in events:
            callback = event_key.data
            callback()


def connected():
    selector.unregister(sock.fileno())
    print('Connected')


# Notify when the socket is writable, denoted by EVENT_WRITE
selector.register(sock.fileno(), EVENT_WRITE, connected)
