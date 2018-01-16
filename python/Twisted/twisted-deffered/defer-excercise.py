import sys
from twisted.internet.defer import Deferred


def got_poem(poem):
    print(poem)
    return 1


def poem_failed(err):
    print("Poem download failed", file=sys.stderr)
    print("Sorry\nTry again later?", file=sys.stderr)


def poem_done(args):
    print(type(args))
    from twisted.internet import reactor
    reactor.stop()

if __name__ == '__main__':
    d = Deferred()

    d.addCallbacks(got_poem, poem_failed)
    # This method registers a same callback for both callback and errback
    d.addBoth(poem_done)

    from twisted.internet import reactor

    reactor.callWhenRunning(d.callback, 'Another short poem')

    reactor.run()

