class Human:

    def sayhello(self, name=None):
        if name is not None:
            print('hello ', name)
        else:
            print('hello')


obj = Human()
obj.sayhello()          # Polymorphism with no parameter
obj.sayhello('John')    # Polymorphism with parameter
