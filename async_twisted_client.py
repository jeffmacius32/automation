from twisted.internet import protocol, reactor
from twisted.internet.pollreactor import connectionDone
from twisted.python.failure import Failure


class EchoClient(protocol.Protocol):
    def connectionMade(self):
        return super().connectionMade()(self)
    self.transport.write(b"hello, world")

    def dataReceived(self, data):
        print("server said", data)
        self.transport.loseConnection()


    def connectionLost(self, reason):
        print("Connection Lost")   
       
    
    