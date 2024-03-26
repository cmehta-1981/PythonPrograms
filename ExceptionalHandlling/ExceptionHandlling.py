print("********************* in built exceptions***************************** ")

# noinspection PyBroadException
try:
    num1, num2 = 10, 0
    result = num1 / num2
    print("result is :- ", result)
except ZeroDivisionError:
    print("Exception ZeroDivisionError occurred")
except SyntaxError:
    print("Syntax error occurred")
except:
    print("Exception handled")
else:
    print("Code is running as expected")
finally:
    print("Finally block executed")

print("********************* user defined exceptions***************************** ")


def numberCheck(num):
    if num < 0:
        raise ValueError("Only integer allowed")  # raise is user defined exception
    if num % 2 == 0:
        print(num, " is even number")
    else:
        print(num, "is odd number")


num = 3
try:
    numberCheck(num)
except ValueError:
    print("Value error exception occurred & handled")
