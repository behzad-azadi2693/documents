from abc import ABCMeta, abstractmethod

#AbstractClass
class Compiler(metaclass = ABCMeta):

    @abstractmethod
    def collectSource(self):
        pass

    @abstractmethod
    def compileToObject(self):
        pass

    @abstractmethod
    def run(self):
        pass

    #TemplateMethod
    def compileAndRun(self):
        self.collectSource()
        self.compileToObject()
        self.run()

#Concrete class
class IOSCompiler(Compiler):

    def collectSource(self):
        print("collecting source code")

    def compileToObject(self):
        print("compiling source code to obj code")

    def run(self):
        print("program running")


ios = IOSCompiler()
ios.compileAndRun()   
