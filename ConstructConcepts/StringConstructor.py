# Requirement :
#   Create one class & Constructor as well as one method
#   Create constructor with three parameter like eid ,ename, esalary
#   Create string constructor to print the eid ,ename , esalary


class MyClass:

    def __init__(self, eid, ename, esalary):
        # local variables assign to class variables which will accessible by display method
        self.eid = eid
        self.ename = ename
        self.esalary = esalary

    def __str__(self):          # create one more string constructor & obly return string value
        return self.ename


obj = MyClass('H100', 'John', 5000000)  # provide the value to constructor
print(obj)                                              # print the values which is provided by constructor
