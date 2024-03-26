class A:

    def m1(self):  # overriden method
        print('this is m1 method from class A')


class B(A):
    def m1(self):
        print('This is m1 method from class B')
        super().m1()   # this is invoked parent class A method m1


obj = B()
obj.m1()  # This is m1 method from class B
