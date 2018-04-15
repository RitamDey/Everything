from twisted.internet import reactor
from twisted.internet import protocol
from twisted.internet import endpoints


class FingerProtocol(protocol.Protocol):
    pass


class FingerFactory(protocol.ServerFactory):
    protocol = FingerProtocol


fingerEndpoint = endpoints.serverFromString(reactor, "tcp:1079")
fingerEndpoint.listen(FingerFactory())
reactor.run()

