class MyClass:
    name = 'CM'

    def __init__(self, name):
        print(self.name)    # print class variable cm
        print(name)         # print constructor value John


obj = MyClass('John')
