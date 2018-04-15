from twisted.internet.defer import Deferred
from twisted.python.failure import Failure


def got_poem(res):
    print("Your poem is saved")
    print(res)


def poem_failed(err):
    print(err)


d = Deferred()

# add a callback/errback pair to the chain
d.addCallbacks(got_poem, poem_failed)

# Fire the chain with an error result
d.errback(Failure(Exception('I have failed.')))


print("Finished")
