from twisted.internet import reactor


def falldown():
    raise Exception('I fall down.')


def upagain():
    print("But I get up again.")
    reactor.stop()


reactor.callWhenRunning(falldown)
reactor.callWhenRunning(upagain)

print("Starting the reactor.")
reactor.run()
