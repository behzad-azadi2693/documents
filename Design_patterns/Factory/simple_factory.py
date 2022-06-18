from abc import ABCMeta, abstractmethod


class Book(classmeta=ABCMeta): #کلاس انتزاعی
    @abstractmethod
    def numberPage(self):
        pass

      
class Python(Book):#subclass
    def numberPage(self):
        print('300')

        
class Django(Book):#subclass
    def numberPage(self):
        print('200')

        
#factory
class PublicFactory():
    def bookPublisher(self, object_type): #متدی که شی رو ایجاد میکنه
        return eval(object_type)().numberPage() #evaluate

      
#client
if __name__ == '__main__':
    pf = PublicFactory()
    book = inputh('which book for print 1-Python 2-Django')
    pf.bookPublisher(book)
