from abc import ABCMeta, abstractmethod


#Subject
class Pardakhtan(metaclass = ABCMeta):

    @abstractmethod
    def do_pay(self):
        pass

#RealSubject
class Bank(Pardakhtan):

    def __init__(self):
        self.card = None
        self.account = None

    def __getAccount(self):
        self.account = self.card
        return self.account

    def __mojoodiDashtan(self):
        print("Bank:: chech mikonad k aya account", self.__getAccount(), "b andaze kafi mojoodi darad ya na")
        return False

    def setCard(self, card):
        self.card = card

    def do_pay(self):
        if self.__mojoodiDashtan():
            print("Bank:: Hazineh pardakht shod")
            return True
        else:
            print("Bank:: Mojoodi Nakafi")
            return False

#Proxy
class Card(Pardakhtan):

    def __init__(self):
        self.bank = Bank()

    def do_pay(self):
        card = input("Proxy:: Shomare Card ra vared kon ")
        self.bank.setCard(card)
        return self.bank.do_pay()

#Client
class You:

    def __init__(self):
        print("You:: Mikham ye pirahan bekharam")
        self.card = Card()
        self.isPurchased = None

    def pardakht(self):
        self.isPurchased = self.card.do_pay()

    def __del__(self):
        if self.isPurchased:
            print("You:: Pirahan ra kharidam")
        else:
            print("You:: poolam baraye kharid pirahan kafi nabood")

you = You()
you.pardakht() 
