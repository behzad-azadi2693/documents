class SingletoneOject(object):
    class __SingletonObject(): #کلاس مدنظر خود را اینجا مینویسیم
        def __init__(self):
            self.value = None

            def __str__(self):
                return self.value

    instance = None #برای نگهداشتن نمونه ساخته شده

    def __new__(cls): #یک کلاس متد است برای بررسی اینکه یک نوع از این کلاس وجود داشته باشد
        if not SingletoneOject.instance: #چک کردن نبود یک نمونه از کلاس 
            SingletoneOject.instance = SingletoneOject.__SingletonObject() # ایجاد یک کلاس نمونه 

        return SingletoneOject.instance # بازگشت کلاس نمونه
    
    def __getattr__(self, MethodNameIn__SingletonObject): #برای دسترسی به درون کلاس پرایویت و فراخواندن متدهای آن
        return getattr(self.instance, MethodNameIn__SingletonObject)

    def __setattr__(self, name, value): #برای دسترسی به درون کلاس پرایویت و ست کردن مقدار جدید برای آن
        return setattr(self.instance, name, value)
