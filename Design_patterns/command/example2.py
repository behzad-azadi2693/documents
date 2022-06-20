from abc import ABCMeta, abstractmethod
#Command
class Order(metaclass = ABCMeta):

    @abstractmethod
    def execute(self):
        pass

#ConcreteCommand
class BuyHouse(Order):

    def __init__(self, house):
        self.house = house

    def execute(self):
        self.house.buy()

class SellHouse(Order):

    def __init__(self, house):
        self.house = house

    def execute(self):
        self.house.sell()

#Reciever
class HouseTrade:

    def buy(self):
        print("shoma khane ra mikharid")

    def sell(self):
        print("shoma khane ra mifrushid")

#Invoker
class Agent:

    def __init__(self):
        self.__orderQueue = []

    def placeOrder(self, order):
        self.__orderQueue.append(order)
        order.execute()

#Client
if __name__ == '__main__':
    house = HouseTrade()
    buyHouse = BuyHouse(house)
    sellHouse = SellHouse(house)

    #invoker
    agent = Agent()
    agent.placeOrder(buyHouse)
    agent.placeOrder(sellHouse)    
