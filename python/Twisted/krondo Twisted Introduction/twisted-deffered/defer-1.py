from twisted.internet.defer import Deferred


def got_poem(res):
    print("Your poem is served")
    print(res)


def poem_failed(err):
    print("No poetry for you")


obj = Deferred()

# Add a callback/errback pair to the chain
obj.addCallbacks(got_poem, poem_failed)

# Fire the chain with a normal result
obj.callback("This poem is short")

print("Finished")
