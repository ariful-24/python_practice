from abc import ABC, abstractmethod


class Computer(ABC):
    @abstractmethod
    def process(self):
        pass
class laptop(Computer):
    def process(self):
        print("Its runnning")




class Programmer:
    def work(self,com):
        print("Solving Bugs")
        com.process()


#com = Computer()
com1 = laptop()
#com.process()

prog1 = Programmer()
prog1.work(com1)