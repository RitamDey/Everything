import traceback
from twisted.internet import reactor


def stack():
    print("The Python Stack.")
    traceback.print_stack()


reactor.callWhenRunning(stack)
reactor.run()
