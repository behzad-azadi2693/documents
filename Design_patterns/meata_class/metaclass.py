class MyInt(type):
    def __call__(self, *args, **kwargs):
        print('new int maked', args)
        return type.__call__(self, *args, **kwargs)


class int(metaclass=MyInt):
    def __init__(self, x, y):
        self.x = x
        self.y = y

a=int(20, 40)


class A: #تفاوت دو کلاس __init__(هنگام ساختن شی), __call__(هنگام صدا زدن شی)
    def __init__(self):
        print('init')

    def __call__(self):
        print('call')

a = A() #__init__
a() #__call__

''' ساخت کلاس توسط پایتون
class B(object):
    def my_func(self):
        pass


B_name = 'B'
B_parent = (object, )
B_attr = {'my_func':my_func}

B = type(name, bases, dict) --> B = tpye(B_name, B_parent, B_attr)
'''
