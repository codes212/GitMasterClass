class Human:
    def __init__(self, name):
        self.name = name
        self.head = self.Head()
        print('Human object creation!')
    def info(self):
        print('My name is', self.name)
        print("I'm busy")
        self.head.talk()
        self.head.brain.think()


    class Head():
            def __init__(self):
                self.brain = self.Brain()
                print('Head object creation!')

            def talk(self):
                print('Talking')


            class Brain():
                def think(self):
                    print('Thinking')
                    print('Brain object creation!')


h  = Human('dhrumil')
h.info()
