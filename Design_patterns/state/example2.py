#State
class MobileState():

    name = "state"
    allowed = []

    def switch(self, state):
        if state.name in self.allowed:
            print("vaziat konooni: ", self, "tagheer yaft be => ", state.name)
            self.__class__ = state
        else:
            print("vaziat konooni: ", self, "tagheer yaft be => ", state.name, "EMKAN PAZIR NIST")

    def __str__(self):
        return self.name

#ConcreteState
class Off(MobileState):
    name = "Off"
    allowed = ['On']

class On(MobileState):
    name = "On"
    allowed = ['Off', 'Restart', 'Airplane']

class Restart(MobileState):
    name = "Restart"
    allowed = ['On']

class Airplane(MobileState):
    name = "Airplane"
    allowed = ['On', 'Off', 'Restart']

#Context
class MobileContext():

    def __init__(self, model='HTC'):
        self.model = model
        self.state = Off()

    def change(self, state):
        self.state.switch(state)


if __name__ == "__main__":
    mob = MobileContext()
    mob.change(On)
    mob.change(Off)
    mob.change(On)
    mob.change(Restart)
    mob.change(On)
    mob.change(Airplane)
