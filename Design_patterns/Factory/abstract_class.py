
from abc import ABCMeta, abstractmethod


class AbstractOperation(metaclass=ABCMeta):
    def __init__(self, operand_a, operand_b):
        self.operand_a = operand_a
        self.operand_b = operand_b
        super().__init__()

    @abstractmethod
    def execute(self):
        pass


class AddOperation(AbstractOperation):
    def execute(self):
        print(self.operand_a + self.operand_b)
        return self.operand_a + self.operand_b


class MultiOperation(AbstractOperation):
    def execute(self):
        print(self.operand_a * self.operand_b)
        return self.operand_a * self.operand_b


ope1 = AddOperation(3, 4)
ope1.execute()

ope2 = MultiOperation(4, 4)
ope2.execute()
