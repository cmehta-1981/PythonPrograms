class A:
    a, b = 10, 20

    def m1(self):
        print(self.a, self.b)


class B(A):       # class A is parent of class B
    c, d = 20, 40

    def m2(self):
        print(self.c, self.d)


obj = A()
obj.m1()


obj1 = B()
obj1.m2()
obj1.m1()

