class Singleton:
    def __new__(cls): #متد ساخت نوع جدید از کلاس
        if not hasattr(cls, "instance"):#متد چک کننده وجود داشتن یک اتریبیوت یا فالس میده یا تورو
            cls.instance = super().__new__(cls) #متدی مورد نظر ما از کلاس والد رو فرامیخونه و جایگذاری میکنه
        return cls.instance
