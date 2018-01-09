from twisted.internet import reactor


def hello():
    print("Hello from the reactor loop!")
    print("Lately I fell like I'm stuck in a rut")


reactor.callWhenRunning(hello)


print("Starting reactor")
reactor.run()
