from abc import ABCMeta, abstractmethod

class State(metaclass = ABCMeta):

    @abstractmethod
    def handling(self):
        pass

class ConcreteState1(State):

    def handling(self):
        print("ConcreteState1")

class ConcreteState2(State):

    def handling(self):
        print("ConcreteState2")

class Context(State):

    def __init__(self):
        self.state = None

    def getState(self):
        return self.state

    def setState(self, state):
        self.state = state

    def handling(self):
        self.state.handling()

context = Context()
state1 = ConcreteState1()
state2 = ConcreteState2()
context.setState(state2)
context.handling()  
