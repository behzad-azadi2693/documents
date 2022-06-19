#Subject(Object)
class Subject:

    def __init__(self):
        self.__observers = []

    def register(self, observer):
        self.__observers.append(observer)

    def notifyEveryOne(self, *args, **kwargs):
        for observer in self.__observers:
            observer.notify(self, *args, **kwargs)

#Observers
class Observer1:

    def __init__(self, subject):
        subject.register(self)

    def notify(self, subject, *args, **kwargs):
        print(type(self).__name__, args, 'az', subject, 'reside ast')


class Observer2:

    def __init__(self, subject):
        subject.register(self)

    def notify(self, subject, *args):
        print(type(self).__name__, args, 'az', subject, 'reside ast')


sub = Subject()
obs1 = Observer1(sub)
obs2 = Observer2(sub)
sub.notifyEveryOne('Warning')
