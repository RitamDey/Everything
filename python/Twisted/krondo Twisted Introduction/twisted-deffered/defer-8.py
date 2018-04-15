import sys
from twisted.internet.defer import Deferred


def got_poem(poem):
    print(poem)
    from twisted.internet import reactor
    reactor.stop()


def poem_failed(err):
    print("Poem download failed", file=sys.stderr)
    print("Sorry", file=sys.stderr)
    print("Try again later?", file=sys.stderr)
    from twisted.internet import reactor
    reactor.stop()


if __name__ == '__main__':
    d = Deferred()
    d.addCallbacks(got_poem, poem_failed)  # Add callback and errback
    from twisted.internet import reactor
    reactor.callWhenRunning(d.callback, "Another poem")
    reactor.run()

