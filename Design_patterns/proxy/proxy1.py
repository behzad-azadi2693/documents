class Player():

    def __init__(self):
        self.hasContract = True

    def occupied(self):
        self.hasContract = True
        print(type(self).__name__, "dar hale hazer ba yek team gharardad darad")

    def available(self):
        self.hasContract = False
        print(type(self).__name__, "baraye in enteghal azad ast")

    def getStatus(self):
        return self.hasContract


class Agent():

    def work(self):
        self.player = Player()
        if self.player.getStatus():
            self.player.occupied()
        else:
            self.player.available()

if __name__ == '__main__':
    a = Agent()
    a.work()
