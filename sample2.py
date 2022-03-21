from functools import reduce
import requests 


def add(a, b):
    c = a + b
    print(c)
add(3,3)
add(3,6)
add(6,9)

# Returning multiple values  by functions
def calc(a,b):
    c = a+b
    d = a-b
    e = a*b
    return c,d,e
x,y,z = calc(3,3)
print(x)
print(y)
print(z)

# nested functions
def msg1(st):
    def msg():
        return "hello world"
    s = st + msg()
    return s
msg1("hey")


# pass by value
def modify(x):
    x=3
    print(x, id(x))
x=10
modify(x)
print(x, id(x))

# pass by reference
def modify(a):
    a.append(5)
    print(a, id(a))
a=[1,2,3,4]
modify(a)
print(a, id(a))

# positional arguments
def add(a, b):
    c = a + b
    print(c)
add(3,3)

# Keyword arguments
def add(a, b):
    c = a + b
    print(c)
add(a=3,b=3)
add(b=6,a=3)

# Default arguments
def add(a,b=3):
    c = a + b
    print(c)
add(a=3)
add(a=3,b=6)

# Arbitrary Arguments
def add(*a):
    sum = 0
    for i in a:
        sum = sum + i
    print(sum)
add(1,2,3)

def names(*name):
    print(name[1])
names("james","karl","jack")

# Keyword Arbitray Arguments 
def names(**name):
      print(name["lname"])
names(fname = "anderson", lname = "james")

# Local and Global Variables
c = 3
def add(a, b):
    c = 6
    x = a + b + c
    print(x)
add(3,3)
print(c)

# Recursion
def recur(k):
    while(k>0):
        result = k*recur(k-1)
        print(result)
recur(3)

# using global keyword as a local keyword
a=11
def myfunction():
    global a
    a=10
    print(a)
myfunction()
print(a)

# lambda function
x = lambda a : a**3
print(x(3))

x = lambda a,b : a+b
print(x(3,3))

# map() function
def mul(a):
    c = a**2
    print(c)
x = (1,2,3,4,5,6)
y = map(mul,x)

# filter() function
fib = [0,1,1,2,3,5,8,13,21,34,55]
result = filter(lambda x: x % 2, fib)

# reduce() function
y = lambda x,y: x*y
x = reduce(y, range(100))
print(x)

# generator function yield() holds sequence of results and returns it later
def gen(n):
    i = 0
    while(i<n):
        yield(i)
        i = i + 1
x = gen(6)
for i in x:
    print(i)

# A program using request module
r = requests.get('https://www.google.com/')
print(r.status_code)
print(r.headers['content-type'])
print(r.text)

 