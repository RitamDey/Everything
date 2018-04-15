# This is the Twisted Get Poetry Now! client, version 3.0.
import optparse
import sys
from twisted.internet.protocol import Protocol, ClientFactory


def parse_args():
    usage = """usage: %prog [options] [hostname]:port ...
            This is the Get Poetry Now! client, Twisted version 3.0
            Run it like this:
            python get-poetry-1.py port1 port2 port3 ...
            If you are in the base directory of the twisted-intro package,
            you could run it like this:
            python twisted-client-3/get-poetry-1.py 10001 10002 10003
            to grab poetry from servers on ports 10001, 10002, and 10003.
            Of course, there need to be servers listening on those ports
            for that to work.
            """

    parser = optparse.OptionParser(usage)

    _, addresses = parser.parse_args()

    if not addresses:
        print(parser.format_help())
        parser.exit()

    def parse_address(addr):
        if ':' not in addr:
            host = '127.0.0.1'
            port = addr
        else:
            host, port = addr.split(':', 1)

        if not port.isdigit():
            parser.error('Ports must be integers.')

        return host, int(port)

    return list(map(parse_address, addresses))


class PoetryProtocol(Protocol):
    poem = ""

    def dataReceived(self, data):
        # Called whenever data is recieved from the transport
        self.poem += data.decode("utf-8")

    def connectionLost(self, reason):
        # Called when the connected host closes the connection on the socket
        # Twisted reactor calls this method with a reason
        # Here it is called with reason twisted.internet.error.ConnectionDone
        # Indicating the connection finished gracefully
        self.poemRecevied(self.poem)

    def poemRecevied(self, poem):
        # This the final method called when the protocol is signalled to close
        # This method calls the factory's `.poem_finished` method
        # Passing the the protocol's task id and the content of poem
        self.factory.poem_finished(poem)


class PoetryClientFactory(ClientFactory):
    protocol = PoetryProtocol

    def __init__(self, callback, errback):
        self.callback = callback
        self.errback = errback  # Failure handling callback

    def poem_finished(self, poem):
        # Called when the the client has finished downloading
        self.callback(poem)

    def clientConnectionFailed(self, connector, reason):
        # Called when the client has encountered some error
        self.errback(reason)


def get_poetry(host, port, callback, errback):
    """
    Downnload a poem from the given host and port and invoke

    callback(poem)

    when the poem is complete. If there is a failure, invoke

    callback(err)

    instead, where err is a twisted.python.failure.Failure instance.
    """
    from twisted.internet import reactor
    factory = PoetryClientFactory(callback, errback)
    reactor.connectTCP(host, port, factory)


if __name__ == '__main__':
    addresses = parse_args()

    from twisted.internet import reactor
    poems = []
    errors = []

    def got_poem(poem):
        poems.append(poem)
        poem_done()

    def poem_done():
        if len(poems) + len(errors) == len(addresses):
            reactor.stop()

    def poem_failed(err):
        print('Poem failed:', err, file=sys.stderr)
        errors.append(err)
        poem_done()

    for address in addresses:
        host, port = address
        get_poetry(host, port, got_poem, poem_failed)

    reactor.run()

    for poem in poems:
        print(poem)
