
class Singleton:#فقط در صورت نیاز قطعی برای ما کلاس میسازه
    __instance = None #اتتریبیوت پرایویت برای نگه داشتن نمونه

    def __init__(self):
        if not Singleton.__instance:#چک کردن وجو داشتن یا نداشتن نمونه مدنظر
            print('we want to create instance...')
        else:
            print("instance class created", Singleton.getInstance)#

    @classmethod
    def getInstance(cls):#متد سازنده نمونه مدنظر ما
        if not cls.__instance:
            cls.__instance = Singleton()
        return cls.__instance
        

s1 = Singleton()
print('obj creates of class ', Singleton.getInstance())
s2 = Singleton()
