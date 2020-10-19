class Customer:
    bankname = 'Axis Bank'
    def __init__(self, name, balance = 0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print('The balance is :', self.balance)

    def withdraw(self, amount):
        if self.balance < amount:
            print('Insufficient funds! please add something!')
        else:
            self.balance = self.balance - amount
            print('The balance is :', self.balance)


name = input('Please enter your name:')
c = Customer(name)
while True:
    print('Welcome to ', c.bankname, name)

    option = input('W,D or Q:')

    if option.lower() == 'd':
        amount = float(input('Enter the amount:'))
        c.deposit(amount)

    elif option.lower() == 'w':
        amount = float(input('Enter the amount:'))
        c.withdraw(amount)

    elif option.lower() == 'q':
        break

    else:
        print('Select a valid option!')