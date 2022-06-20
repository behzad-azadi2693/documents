from abc import ABCMeta, abstractmethod

class AbstractClass(metaclass = ABCMeta):

    def __init__(self):
        pass

    @abstractmethod
    def operation1(self):
        pass

    @abstractmethod
    def operation2(self):
        pass

    @abstractmethod
    def operation3(self):
        pass

    def templateMethod(self):
        print("Tartib amaliat in shekli mibashad:aval: operation2, dovom: operation3, sevom: operation1")
        self.operation2()
        self.operation3()
        self.operation1()


class ConcreteClass(AbstractClass):

    def operation1(self):
        print("operation1 anjam shod")

    def operation2(self):
        print("operation2 anjam shod")

    def operation3(self):
        print("operation3 anjam shod")


#Client
class Client():

    def action(self):
        self.concreteClass = ConcreteClass()
        self.concreteClass.templateMethod()

client = Client()
client.action()      
