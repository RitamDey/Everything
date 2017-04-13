import socket
from selectors import DefaultSelector, EVENT_WRITE, EVENT_READ


selector = DefaultSelector()


def loop():
    while True:
        events = selector.select()
        for event_key, event_mask in events:
            callback = event_key.data
            callback()


class Fetcher:
    def __init__(self, url):
        self.response = b''
        self.url = url
        self.sock = None

    def fetch(self):
        """
        * This method is used to create a non-blocking socket
        * Then it tries to connect to the website
        * If it recieves a BlockingIOError then it gives up
        * If the connection is succesful the its awaits for a event
        * Which is handled by the connected method callback
        """
        self.sock = socket.socket()
        self.sock.setblocking(False)

        try:
            self.sock.connect(('xkcd.com', 80))
        except BlockingIOError:
            pass

        # Register next callback
        selector.register(self.sock.fileno(),
                          EVENT_WRITE,
                          self.connected)

    def connected(self, key, mask):
        """
        * This method is used to send a GET request to the url
        * It sents a requests and awaits for the sent event to complete
        * And for the read event we register a new callback
        """
        print("Connected!")
        selector.unregister(key.fd)
        request = f'GET {self.url} HTTP/1.0\r\nHost: xkcd.com\r\n\r\n'
        self.sock.send(request.encode('ascii'))

        # Register the next callback
        selector.register(key.fd,
                          EVENT_READ,
                          self.read_response)

    def read_response(self, key, mask):
        global stopped

        chunk = sock.recv(4096)  # 4K chunk size
        if chunk:
            response += chunk
        else:
            selector.unregister(key.fd)  # Done reading
            links = set()
            links = self.parse_links()

        # Python set logic
        for link in links.difference(seen_urls):
            urls_todo.add(link)
            Fetcher(link).fetch()  # <- New fetcher for th urls

        seen_urls.update(links)
        urls_todo.remove(self.url)
        if not urls_todo:
            stopped = True


# Page is now downloaded
links = parse_links(response)
q.add(links)


urls_todo = set(['/', ])
seen_urls = set(['/', ])
