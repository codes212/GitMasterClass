class P:
    def m1(self):
        print('Parent method!')


class C(P):
    def m2(self):
        print('Child1 method!')


class CC(C):
    def m3(self):
        print('Child2 method!')


c = CC()
c.m1()
c.m2()
c.m3()
