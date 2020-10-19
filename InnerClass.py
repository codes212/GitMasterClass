class Outer:

    def __init__(self):
        print('Outer method created!')

    class Inner:
        def __init__(self):
            print('Inner method created!')

        def m1(self):
            print('Jay jinendra! Dhrumil Sanghvi')

i = Outer().Inner().m1()

