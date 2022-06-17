class Monostate: #کلاسی برای برگرداند حالت ثابت چند نمونه مختلف
    _shared_state = {'y':'200'} #ایجاد یک حالت اولیه با مقدار پیش فرض

    def __init__(self): #متد سازنده پایتون
        self.x = '25o'
        self.__dict__ = self._shared_state #اشتراک حالت عمومی  ثابت پایتون برای تمامی نمونه های مختلف

a1 = Monostate()
a2 = Monostate()
a1.x = '300'

print(a1, a2)
print(a1.__dict__, a2.__dict__)
