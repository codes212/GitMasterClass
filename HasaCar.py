class Car:
    def __init__(self, model, version, color):
        self.model = model
        self.version = version
        self.color = color

    def getinfo(self):
        print('CarModel: {} Version: {}, Color:{}'.format(self.model, self.version, self.color))


class Employee:
    def __init__(self, ename, eno, car):
        self.ename = ename
        self.eno = eno
        self.car = car

    def getemployeeinfo(self):
        print('Employee Name:{}, Employee number: {}'.format(self.ename, self.eno))
        car.getinfo()


car = Car('Honda', '2.5V', 'Black')
e = Employee('Dhrumil', 206, car)
e.getemployeeinfo()

