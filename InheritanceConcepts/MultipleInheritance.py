class A:
    a, b = 10, 20

    def m1(self):
        print(self.a + self.b)


class B:  # class A is parent of class B
    c, d = 40, 30

    def m2(self):
        print(self.c - self.d)


class C(A, B):
    x, y = 50, 60

    def m3(self):
        print(self.x * self.y)


obj = C()
obj.m1()
obj.m2()
obj.m3()
