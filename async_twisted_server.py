from twisted.internet import protocol, reactor

class Echo(protocol.Protocol):
    def dataReceived(sefl, data):
        print(data)
        self.transport.write(data)


def main():
    factory = protocol.ServerFactory()
    factory.protocol = Echo
    reactor.listenTCP(8000, factory)
    reactor.run()


if __name__ == "__main__":
    main()
          