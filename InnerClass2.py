class Human:
    def __init__(self, name):
        self.name = name
        self.head = self.Head()
        print('Human object created!')

    def info(self):
        print('Hello,', self.name)
        print("I'm very busy!")
        self.head.talk()
        self.head.brain.think()

    class Head:
        def __init__(self):
            self.brain = self.Brain()
            print('Head object created!')

        def talk(self):
            print('Talking!')

        class Brain:
            def __init__(self):
                print('Brain object created!')

            def think(self):
                print('Thinking! ')


p = Human('Dhrumil')
p.info()
