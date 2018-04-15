from twisted.internet.defer import Deferred


def out(s):
    print(s)


d = Deferred()
d.addCallbacks(out, out)

d.callback('First Result')
d.callback('Second Result')  # Will fail complaning Deferred already called

print("Finished")
