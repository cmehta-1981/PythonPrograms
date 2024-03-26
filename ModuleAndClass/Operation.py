# calling functions from calculator module

# approach 1
import Calculator

Calculator.add(10, 20)
Calculator.mul(10, 10)

# approach 2

from Calculator import add, mul

add(20, 30)
mul(20, 30)


# approach 3

from Calculator import *
add(30,40)
mul(30,40)