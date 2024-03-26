# Requirement :
#   Create one class & Constructor as well as one method
#   Create constructor with three parameter like eid ,ename, esalary
#   Create display() to print the eid ,ename , esalary


class MyClass:

    def __init__(self, eid, ename, esalary):
        # local variables assign to class variables which will accessible by display method
        self.eid = eid
        self.ename = ename
        self.esalary = esalary

    def display(self):
        print('print the eid , ename & esalary: -', self.eid, self.ename, self.esalary)


obj = MyClass('H100', 'John', '50k')    # provide the value to constructor
obj.display()                                              # print the values which is provided by constructor

obj1 = MyClass('H101', 'Jack', '70k')
obj.display()
