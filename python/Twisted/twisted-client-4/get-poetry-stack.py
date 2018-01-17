import optparse
import sys
import os
import traceback
from twisted.internet import defer
from twisted.internet.protocol import Protocol, ClientFactory


def parse_args():
    usage = """usage: %prog [options] [hostname]:port ...
            This is the Get Poetry Now! client, Twisted version 4.0
            Run it like this:
            python get-poetry.py port1 port2 port3 ...
            If you are in the base directory of the twisted-intro package,
            you could run it like this:
            python twisted-client-4/get-poetry.py 10001 10002 10003
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

    def dataReceived(self, data: bytes):
        self.poem += data.decode("utf-8")

    def connectionLost(self, reason):
        self.poemReceived(self.poem)

    def poemReceived(self, poem):
        self.factory.peom_finished(poem)


class PoetryClientFactory(ClientFactory):
    protocol = PoetryProtocol

    def __init__(self, deferred):
        self.deferred = deferred

    def peom_finished(self, poem):
        if not self.deferred.called:
            self.deferred.callback(poem) 

    def clientConnectionFailed(self, connector, reason):
        if not self.deferred.called:
            self.deferred.errback(reason)


def get_poetry(host, port):
    """
    Download a poem from the given host and port. This function
    returns a Deferred which will be fired with the complete text
    of the poem or a Failure if the poem could not be downloaded
    """
    d = defer.Deferred()

    from twisted.internet import reactor

    factory = PoetryClientFactory(d)
    reactor.connectTCP(host, port, factory)
    return d


if __name__ == '__main__':
    addresses = parse_args()

    from twisted.internet import reactor

    poems = []
    errors = []

    def got_poem(poem):
        traceback.print_stack()
        os._exit(0)

    def poem_failed(err):
        print("Poem failed:", err, file=sys.stderr)
        errors.append(err)

    def poem_done(_):
        if len(poems)+len(errors) == len(addresses):
            reactor.stop()


    for address in addresses:
        host, port = address
        d = get_poetry(host, port)
        d.addCallbacks(got_poem, poem_failed)
        d.addBoth(poem_done)

    reactor.run()

    for poem in poems:
        print(poem)

