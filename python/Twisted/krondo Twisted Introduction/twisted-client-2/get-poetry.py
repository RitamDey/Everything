# This is the Twisted Get Poetry Now! client, version 2.0
import datetime
import optparse
from twisted.internet.protocol import Protocol, ClientFactory


def parse_args():
    usage = """usage: %prog [options] [hostname]:port ...
    This is the Get Poetry Now! client, Twisted version 2.0.
    Run it like this:
    python get-poetry.py port1 port2 port3 ...
    If you are in the base directory of the twisted-intro package,
    you could run it like this:
    python twisted-client-2/get-poetry.py 10001 10002 10003
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
    poem = b""
    task_num = 0

    def dataReceived(self, data):
        # Called whenever data is recieved from the transport
        self.poem += data
        msg = "Task %d: got %d bytes of poetry from %s:%s"

        # The `.transport` is the network transporter object that the Protocol is using
        # The `.transport.getPeer()` return a object of the connected IP Address <class twisted.internet.address.IPv4Address>
        # The returned object has two fields `.host` and `.port` contains the connected host IP and port number
        print(msg %(self.task_num, len(data), self.transport.getPeer().host, self.transport.getPeer().port))

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
        self.factory.poem_finished(self.task_num, poem)


class PoetryClientFactory(ClientFactory):
    task_num = 1  # Initial task id
    protocol = PoetryProtocol  # Tell the base-classes to use this protocol

    def __init__(self, poetry_count):
        self.poetry_count = poetry_count
        self.poems = {}  # task_num -> poem content

    def buildProtocol(self, address):
        # Create a object of the Protocol
        # The returned instance will handle input on an incoming server
        # connection, and an attribute "factory" pointing to the creating
        # factory.
        
        # Alternatively, L{None} may be returned to immediately close the
        # new connection.

        # Call the base-class's buildProtocol since our Protocol is basic
        proto = ClientFactory.buildProtocol(self, address)
        proto.task_num = self.task_num  # Assign the new protocol its id
        self.task_num += 1  # Increment the id
        return proto  # Return the built protocol

    def poem_finished(self, task_num=None, poem=None):
        # Called when a proocol finishes downloading data from server
        if task_num is not None:
            # Use the passed task id to populate the poem it fetched
            self.poems[task_num] = poem

        self.poetry_count -= 1  # Decrement the count of active tasks

        if self.poetry_count == 0:  # Case used when all tasks are finished
            self.report()
            # Call the Twisted's reactor and stop it since all the
            # newtworking task has been finished
            from twisted.internet import reactor
            reactor.stop()

    def report(self):
        for i in self.poems:
            print("Task %d: %d bytes of poetry" %(i, len(self.poems[i])))

    def clientConnectionFailed(self, connector, reason):
        # This method is called when the object fails to connect to the server
        # This method is called with a connector object representing the 
        # connection's protocol type (here TCP) and a reason object

        # Use the connector's `.getDestination` object to get the destination
        # address repesented in the correspoing IPv4/IPv6 object
        dest = connector.getDestination()
        # Get the host and port number from it
        print("Failed to connect to: %s:%s" %(dest.host, dest.port))

        # Use the reason object to get the actual error object
        # and the actual error message
        # Since multiple error can error, they are passed in a typle object
        print("Reason is:", *reason.args[0].args)

        # Call the `.poem_finished` since the client has terminated
        self.poem_finished()


if __name__ == '__main__':
    addresses = parse_args()

    start = datetime.datetime.now()

    factory = PoetryClientFactory(len(addresses))  

    from twisted.internet import reactor

    for address in addresses:
        # Get the host and port from the returned tuples
        host, port = address
        # The .connectTCP method is of interest here.
        # It takes the host and port as first two parameter
        # And also a protocol factory to create the protocol objects on-demand
        reactor.connectTCP(host, port, factory)

    reactor.run()

    elapsed = datetime.datetime.now() - start

    print("Got %d poems in %s" %(len(addresses), elapsed))
