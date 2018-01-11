# Twisted Get Poetry Client version 1.0
import datetime
import errno
import optparse
import socket
from twisted.internet import main


def parse_args():
    usage = """usage: %prog [options] [hostname]:port ...
            This is the Get Poetry Now! client, Twisted version 1.0.
            Run it like this:
            python get-poetry.py port1 port2 port3 ...
            If you are in the base directory of the twisted-intro package,
            you could run it like this:
            python twisted-client-1/get-poetry.py 10001 10002 10003
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

    return map(parse_address, addresses)


class PoetrySocket:
    def __init__(self, task_num, address):
        from twisted.internet import reactor
        self.poem = b""  # The poem holder
        self.task_num = task_num  # Task identifier assigned
        self.address = address  # The address to connect
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # cancel_handle is used to schedule a callback to self.connectionLost
        # ,with the reason of main.CONNECTION_LOST, 2 seconds into the future
        # thus effectively acting as a timeout task
        self.cancel_handle = reactor.callLater(60, self.connectionLost, main.CONNECTION_LOST)
        try:
            self.sock.connect(address)  # Connect to the address
            self.sock.setblocking(0)  # Making it a non-blocking socket
            
            # Tell the Twisted reactor to monitor this socket for reading
            reactor.addReader(self)  # Monitor for reading
        except:
            print("Can't connect to", address)
            return

    def fileno(self):
        # Method for iterface IFileDescriptor
        # Used to identify and work with the UNIX style numeric file descriptor
        try:
            return self.sock.fileno()  # Try to return the UNIX socket file descriptor
        except socket.error:
            # If we are here, then it means that there is a malformed socket
            # Return a standard -1 descriptor
            return -1

    def connectionLost(self, reason):
        # Called when the connection is lost

        # This is called when the connection on a selectable object has been
        # lost.  It will be called whether the connection was closed explicitly,
        # an exception occurred in an event handler, or the other end of the
        # connection closed it first.
        
        self.sock.close()  # Close the socket and its associated file descriptor

        # stop monitoring this socket
        from twisted.internet import reactor
        reactor.removeReader(self)  # Remove this object from the monitored reader FDs

        # see if there are any poetry sockets left
        for reader in reactor.getReaders():
            if isinstance(reader, PoetrySocket):
                return

        reactor.stop()  # no more readers, no more poetry

    def doRead(self):
        read_bytes = b""  # Currently read bytes

        while  True:
            try:
                bytesread = self.sock.recv(1024)  # Try to read 1024 bits
                if not bytesread:
                    break
                else:
                    read_bytes += bytesread
            except socket.error as e:
                # If a error is raised
                # then check if the operation would cause socket blocking
                if e.args[0] == errno.EWOULDBLOCK:
                    break
                # If not then just return a Twisted error saying 
                # connection of the socket has lost
                return main.CONNECTION_LOST

        if not read_bytes:
            # If nothing has been transmitted then the server finished
            # sending data, just print the task number and return saying
            # the connecton purpose has been served
            print("Task %d finished" %(self.task_num))
            return main.CONNECTION_DONE  # Indicate connection completed
        else:
            msg = "Task %d: got %d bytes of poetry from %s"
            print(msg %(self.task_num, len(read_bytes), self.format_addr()))

        self.poem += read_bytes  # If we are here, just append the data

    def logPrefix(self):
        # Method implemented for the ILoggingContext Interface
        # @return: The prefix for the logger system
        return "poetry"

    def format_addr(self):
        host, port = self.address
        return "%s:%s" %(host or "127.0.0.1", port)


def poetry_main():
    addresses = list(parse_args())

    start = datetime.datetime.now()

    sockets = [PoetrySocket(i+1, addr) for i, addr in enumerate(addresses)]

    from twisted.internet import reactor
    reactor.run()

    elapsed = datetime.datetime.now() - start

    for i, sock in enumerate(sockets):
        print("Task %d: %d bytes of poetry" %(i+1, len(sock.poem)))

    print("Got %d poems in %s" %(len(addresses), elapsed))


if __name__ == '__main__':
    poetry_main()
