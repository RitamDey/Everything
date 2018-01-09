from twisted.internet import reactor


class Counter:
    counter = 5

    def count(self):
        if self.counter == 0:
            reactor.stop()
        else:
            print(self.counter, "...")
            self.counter -= 1
            # .callLater takes two arguments:
            # The time delay in seconds, the timeout value for select call
            # The function object to call
            reactor.callLater(1, self.count)


reactor.callWhenRunning(Counter().count)
print("Start!")
reactor.run()
print("Stop!")
