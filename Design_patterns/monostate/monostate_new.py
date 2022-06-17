class MonostateNew: #کلاسی برای برگرداند حالت ثابت چند نمونه مختلف با کلاس سازنده
    _shared_state = {} #ایجاد یک حالت اولیه با مقدار پیش فرض خالی

    def __new__(cls, *args, **kwargs): #متد سازنده نمونه جدید کلاس با دریافت لیست آرگومان و کلیدی آرگومانی
        obj = super().__new__(cls, *args, **kwargs) #فراخواندن متد کلاس والد برای اجرا متد مدنظر و مقدار اولیه در متد
        obj.__dict__ = cls._shared_state #اشتراک حالت عمومی  ثابت پایتون برای تمامی نمونه های مختلف
        return obj #برگرداندن نمونه
 
a1 = Monostate()
a2 = Monostate()
a1.x = '300'

print(a1, a2)
print(a1.__dict__, a2.__dict__)    
