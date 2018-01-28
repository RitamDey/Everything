"""
An example script that demonstrates the effect of unhandled
Failure occuring the last callback of the Deferred chain
"""
from twisted.internet.defer import Deferred


def callback(res):
    raise Exception('oops')


if __name__ == '__main__':
    d = Deferred()
    d.addCallback(callback)
    d.callback("Here is the result")
    print("Finished")
