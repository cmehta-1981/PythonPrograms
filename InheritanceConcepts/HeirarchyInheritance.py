class A:
    a, b = 10, 20

    def m1(self):
        print(self.a + self.b)


class B(A):  # class A is parent of class B
    c, d = 40, 30

    def m2(self):
        print(self.c - self.d)


class C(A):
    x, y = 50, 60

    def m3(self):
        print(self.x * self.y)


obj = B()
obj.m2()
obj.m1()

obj1 = C()
obj1.m1()
obj1.m3()
