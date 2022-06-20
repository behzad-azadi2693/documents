from abc import ABCMeta, abstractmethod

#AbstractClass
class Mosaferat(metaclass = ABCMeta):

    @abstractmethod
    def rooz1(self):
        pass

    @abstractmethod
    def rooz2(self):
        pass

    @abstractmethod
    def rooz3(self):
        pass

    @abstractmethod
    def bazgasht(self):
        pass

    #TemplateMethod
    def barnameSafar(self):
        self.rooz1()
        self.rooz2()
        self.rooz3()
        self.bazgasht()

#ConcreteClass
class SafareShiraz(Mosaferat):

    def rooz1(self):
        print("zyarate SHAHCHERAGH")

    def rooz2(self):
        print("hafezie va saadie")

    def rooz3(self):
        print("Baghe afifiabad va bagh eram")

    def bazgasht(self):
        print("bazgasht az Safare Shiraz")


class SafareEsfahan(Mosaferat):

    def rooz1(self):
        print("Midane naghshe jahan")

    def rooz2(self):
        print("40 sotoon")

    def rooz3(self):
        print("33 pol va pol khajoo")

    def bazgasht(self):
        print("bazgasht az Safare Esfahan")


class TravelAgency:

    def tartibDadaneSafar(self):
        maghsad = input("Kodoom shahr mikhayd berid? shiraz ya esfahan?")
        if maghsad == 'shiraz':
            self.safar = SafareShiraz()
            self.safar.barnameSafar()

        if maghsad == 'esfahan':
            self.safar = SafareEsfahan()
            self.safar.barnameSafar()


TravelAgency().tartibDadaneSafar()
