from twisted.internet import pollreactor
from twsited.internet import reactor


pollreactor.install()  # Install the Polling reactor
reactor.run()  # Runs the Polling Reactor since its installed
