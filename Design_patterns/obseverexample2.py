from abc import ABCMeta, abstractmethod
#Subject
class Publisher:

    def __init__(self):
        self.__subscribers = []
        self.__latestBooks = None

    def register(self, subscriber):
        self.__subscribers.append(subscriber)

    def deregister(self):
        return self.__subscribers.pop()

    def subscribers(self):
        return [type(s).__name__ for s in self.__subscribers]

    def notifySubscribers(self):
        for sub in self.__subscribers:
            sub.update()

    def addBooks(self, books):
        self.__latestBooks = books

    def getBooks(self):
        return "Taze haye enteshar: ", self.__latestBooks

#Observer
class Subscriber(metaclass = ABCMeta):

    @abstractmethod
    def update(self):
        pass

#ConcreteObserver1
class SMSSubscriber:

    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.register(self)

    def update(self):
        print(type(self).__name__, self.publisher.getBooks())

#ConcreteObserver2
class EmailSubscriber:

    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.register(self)

    def update(self):
        print(type(self).__name__, self.publisher.getBooks())

#ConcreteObserver3
class AnyOtherSubscriber:

    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.register(self)

    def update(self):
        print(type(self).__name__, self.publisher.getBooks())


if __name__ == '__main__':
    pub = Publisher()
    for Subscribers in [SMSSubscriber, EmailSubscriber, AnyOtherSubscriber]:
        Subscribers(pub)
    print("\nSubscribers: ", pub.subscribers())
    pub.addBooks("Advanced python")
    pub.notifySubscribers()
    print("\nUnregistered :", type(pub.deregister()).__name__)
    print("\nSubscribers: ", pub.subscribers)
