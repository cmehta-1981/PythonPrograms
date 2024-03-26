# calling module ClassA & ClassB to access the methods

# approach 1

import ClassA
import ClassB

obj1 = ClassA.Animal()
obj1.fly()

obj2 = ClassB.Bird()
obj2.fly()

# approach 2

from ClassA import Animal
from ClassB import Bird

obj1 = Animal()
obj1.fly()

obj2 = Bird()
obj2.fly()

