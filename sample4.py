#print(3/0)
''' "ZeroDivisionError" since the number is being divided by 0 '''

# b = [1,2,3,4]
# print(b[6])
''' "IndexError" since it is out of index '''

# a + b
''' "NameError" since the variables are not declared '''

# int('333.333')
''' "ValueError" since invalid literal '''

# '3'*'3'
''' "TypeError" since cant multiply strings '''

from __future__ import division
from signal import raise_signal
from typing import final


try:
    '3'*'3'
except TypeError:
    pass
print("Hello World")

try:
    print(3/0)
except ZeroDivisionError:
    print("Cant divide with zero")
print("heyyyy yo")

try:
    print(3/0)
except ZeroDivisionError as msg:
    print("Cant divide with zero", msg)
print("heyyyy yo")

try:
    print(3/0)
except ZeroDivisionError as msg:
    print("Cant divide with zero", msg)
finally:
    print("blahh")     # irrespective to code execution finally always executes
    

try:
    a = int(input("enter number1"))
    b = int(input("enter number2"))
    c = a/b
    print(c)
    if b == 0:
        raise ("Cant divide with zero")
    else:
        raise ("can divide")
except:
    pass

