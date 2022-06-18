class MetaSingleton:
  _instance = {} #_instance = {"--":"--",...}
  
  def __call__(cls, *args, **kwargs):
    if cls not in cls._instance:
      cls._instance[cls] = super().__call__(*args, **kwargs) #_instance = {"cls":"super().__call__(*args, **kwargs)"}
    return cls._instance[cls]
  
class Logger(metaclass=MetaSingleton):
  pass

L1 = Logger()
L2 = Logger()

print(L1, L2)
