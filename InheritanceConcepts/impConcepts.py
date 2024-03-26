class A:
    a, b = 10, 20


class B(A):
    a, b = 30, 40

    def m1(self, a, b):
        print('add local variables', (a + b))
        print('add class variables', (self.a + self.b))
        print('add parent class variables ', (A.a + A.b))
        print('add parent class variables' , (super().a+super().b))


obj = B()
obj.m1(50, 60)
