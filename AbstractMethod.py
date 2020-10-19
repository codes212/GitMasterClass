from abc import *

class Test(ABC):
    @abstractmethod
    def m1(self):
        pass

class subtest(Test):
    pass


# s = subtest()

t = Test()



