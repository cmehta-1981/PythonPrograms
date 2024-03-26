#   class is collection of variables(attributes) & methods (behaviour)
#   class is blueprint & its is a logical entity
#   class does not occupy space in the memory
#   object is instance of class
#   object is physical entity & occupy space in memory
#   many object can be created in single class & all are independent to each other
#   instance method can call through object only
#   static method can directly call using its class
#   function can create without class however method can create inside the class


i, j = 5, 10  # global variables

class TestClass:
    a, b = 10, 20  # this is class variables

    def div(self):
        print(self.a % self.b)  # print class variables
        print('print global variables : ', i, j)  # print global variables

    def mode(self):
        a, b = 10, 20  # local variables
        print(a / b)


    def myFun(self):
        pass

    def display(self):
        print("this is first line ")

    def display_name(self, name):
        print(name)

    def __init__(self):  # constructor defined & print the value once class object created
        print('constructor called ')

    @staticmethod
    def add(num1, num2):  # self parameter is not mandatory for static method
        print(num1 + num2)

    def mul(self, num1, num2):  # static method with self parameter
        print(self * num1 * num2)


obj = TestClass()
obj.div()
obj.mode()
obj.display()
obj.myFun()
obj.display_name('John')
TestClass.add(10, 20)  # add method called by class name only
TestClass.mul(10, 20, 30)  # mul method called by class name only & also pass the value of self
