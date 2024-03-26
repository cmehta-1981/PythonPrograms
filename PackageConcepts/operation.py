# want to access modules from package pack1

import sys

#approach 1
sys.path.append("C:/Users/ermam/PycharmProjects/pythonProject/PackageConcepts/pack1")

import module1
import module2

module1.animal()
module2.bird()

#approach 2
from module1 import *
from module2 import *

animal()
bird()
